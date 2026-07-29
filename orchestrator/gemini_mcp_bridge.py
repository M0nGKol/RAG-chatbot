"""Bridges Gemini function-calling to the Neo4j MCP server.

Gemini doesn't speak MCP natively, so this glue does three things:
  1. Launches the Neo4j MCP server as a subprocess and opens an MCP session
     over stdio.
  2. Lists the server's tools (e.g. search/cypher/schema tools) and converts
     each one into a Gemini FunctionDeclaration.
  3. Runs the request/response loop: send the user's message to Gemini: if
     Gemini responds with a function call, execute it against the MCP
     session, feed the result back, repeat until Gemini returns text.

One GraphRAGOrchestrator instance holds one MCP session (one Neo4j
connection) and one chat history per Telegram user.
"""
from __future__ import annotations

import asyncio
import logging
import os
from contextlib import AsyncExitStack

from google import genai
from google.genai import errors as genai_errors
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.exceptions import McpError

from common.config import Settings
from orchestrator.schema_convert import json_schema_to_genai_schema

log = logging.getLogger("orchestrator")

# mcp's ClientSession.call_tool() has NO timeout by default -- it will await
# a response from the MCP server subprocess forever. If that subprocess (or
# the Aura instance it's querying) ever stalls -- a slow/cold query, Aura
# waking up from idle, a network hiccup -- this call hangs indefinitely.
# Because python-telegram-bot processes updates sequentially by default,
# ONE stuck tool call freezes the bot for every user until it's manually
# restarted. This timeout turns that into a clean error instead.
#
# Applied via asyncio.wait_for rather than call_tool's own
# read_timeout_seconds parameter: that parameter doesn't exist in
# mcp 1.1.2 (the version pinned in requirements.txt) and passing it raises
# TypeError. wait_for works on every mcp version.
MCP_TOOL_TIMEOUT_SECONDS = 45

# google-genai's Chat.send_message() is a SYNCHRONOUS network call. Calling
# it directly inside an `async def` blocks the entire asyncio event loop
# thread for as long as it takes -- not just this one user's request, but
# the whole process: every other user's message, Telegram's own polling
# loop, and even the MCP_TOOL_TIMEOUT above (asyncio timeouts need the loop
# to keep running to fire at all). It's run via asyncio.to_thread() below so
# a slow/stuck Gemini call only ties up one worker thread, not everything.
# GEMINI_REQUEST_TIMEOUT_MS is a belt-and-suspenders HTTP-level timeout on
# top of that, so a stuck thread still eventually gives up instead of
# hanging forever.
GEMINI_REQUEST_TIMEOUT_MS = 30_000

# Gemini occasionally returns transient 5xx errors (504 DEADLINE_EXCEEDED,
# 503 UNAVAILABLE) that have nothing to do with the request itself -- retry
# those a couple of times with a short backoff before giving up, so a random
# server-side hiccup doesn't surface as a failure to the user at all.
GEMINI_MAX_RETRIES = 2
GEMINI_RETRY_BACKOFF_SECONDS = 2

# 429 RESOURCE_EXHAUSTED is quota, not a transient fault, so it's handled
# separately: Google tells us how long to wait in the error payload
# (RetryInfo.retryDelay), so we honor that rather than guessing. If the wait
# is longer than this cap, there's no point stalling a Telegram user -- give
# up and tell them plainly. NOTE: free-tier quotas are PER DAY as well as
# per minute, and a per-day exhaustion won't clear no matter how long we
# wait, so waiting a long time here would be pointless anyway.
GEMINI_MAX_QUOTA_WAIT_SECONDS = 30

SYSTEM_INSTRUCTION = """You are a helpful assistant answering questions using \
a Neo4j knowledge graph as your source of truth. You have tools available to \
search and query that graph -- use them before answering any question that \
depends on the knowledge base rather than guessing. If the tools return \
nothing relevant, say plainly that you don't have that information yet \
instead of making something up. Keep answers concise and suited for a \
Telegram chat."""


class QuotaExceededError(Exception):
    """Gemini API quota/rate limit is exhausted and waiting won't help soon.

    Raised instead of leaking a raw ClientError so the Telegram layer can
    show users something meaningful rather than a generic failure.
    """


def _retry_delay_seconds(err) -> float | None:
    """Extract Google's own suggested retry delay from a 429 payload.

    The error details carry a RetryInfo entry like {'retryDelay': '22s'} --
    honoring it is far better than guessing a backoff, since Google knows
    when the quota window actually rolls over.
    """
    details = getattr(err, "details", None)
    if not isinstance(details, dict):
        return None
    for item in details.get("error", {}).get("details", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("@type", "")).endswith("RetryInfo"):
            raw = str(item.get("retryDelay", "")).strip()
            if raw.endswith("s"):
                try:
                    return float(raw[:-1])
                except ValueError:
                    return None
    return None


class GraphRAGOrchestrator:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.genai_client = genai.Client(
            api_key=settings.google_api_key,
            http_options=types.HttpOptions(timeout=GEMINI_REQUEST_TIMEOUT_MS),
        )
        self._stack = AsyncExitStack()
        self.mcp_session: ClientSession | None = None
        self._gemini_tool: types.Tool | None = None
        self._chats: dict[str, "genai.chats.Chat"] = {}
        self._system_instruction = SYSTEM_INSTRUCTION

    async def start(self) -> None:
        server_params = StdioServerParameters(
            command=self.settings.mcp_server_command,
            args=[],
            # Merge onto the current environment rather than replacing it --
            # passing env= to a subprocess REPLACES the whole environment,
            # and without PATH in it the OS can't resolve a bare executable
            # name like "neo4j-mcp-server" at all (FileNotFoundError).
            env={
                **os.environ,
                "NEO4J_URI": self.settings.neo4j_uri,
                "NEO4J_USERNAME": self.settings.neo4j_username,
                "NEO4J_PASSWORD": self.settings.neo4j_password,
                "NEO4J_DATABASE": self.settings.neo4j_database,
            },
        )
        read, write = await self._stack.enter_async_context(stdio_client(server_params))
        self.mcp_session = await self._stack.enter_async_context(ClientSession(read, write))
        await self.mcp_session.initialize()

        tools_result = await self.mcp_session.list_tools()
        declarations = [
            types.FunctionDeclaration(
                name=tool.name,
                description=tool.description or "",
                parameters=json_schema_to_genai_schema(tool.inputSchema),
            )
            for tool in tools_result.tools
        ]
        self._gemini_tool = types.Tool(function_declarations=declarations)
        log.info("MCP server exposed %d tool(s): %s", len(declarations), [t.name for t in tools_result.tools])

        await self._preload_schema(tools_result.tools)

    async def _preload_schema(self, tools) -> None:
        """Fetch the graph schema once at startup and bake it into the system
        instruction.

        Without this, Gemini calls get-schema at the start of essentially
        every new conversation just to learn the node labels -- an extra
        API round trip per chat, which matters a lot on quota-limited tiers
        where each request counts. Fetching it once here is free (MCP/Neo4j
        calls aren't rate limited by Google) and removes that round trip.
        """
        if not any(t.name == "get-schema" for t in tools):
            return
        try:
            result = await asyncio.wait_for(
                self.mcp_session.call_tool("get-schema", {}),
                timeout=MCP_TOOL_TIMEOUT_SECONDS,
            )
            schema_text = _tool_result_to_text(result)
        except (McpError, asyncio.TimeoutError) as e:
            # Non-fatal: Gemini can still call get-schema itself at runtime.
            log.warning("Could not preload graph schema (will fall back to runtime calls): %s", e)
            return

        self._system_instruction = (
            f"{SYSTEM_INSTRUCTION}\n\n"
            "Here is the current schema of the knowledge graph, so you do NOT "
            "need to call get-schema before querying -- go straight to "
            "read-cypher for actual content:\n"
            f"{schema_text}"
        )
        log.info("Preloaded graph schema into the system instruction (%d chars)", len(schema_text))

    async def stop(self) -> None:
        await self._stack.aclose()

    def _get_chat(self, session_id: str):
        if session_id not in self._chats:
            self._chats[session_id] = self.genai_client.chats.create(
                model=self.settings.gemini_model,
                config=types.GenerateContentConfig(
                    system_instruction=self._system_instruction,
                    tools=[self._gemini_tool],
                ),
            )
        return self._chats[session_id]

    async def _send_message(self, chat, content):
        """chat.send_message, off the event loop thread, with retries on
        transient Gemini server errors and on 429 quota errors (the latter
        using Google's own suggested delay)."""
        for attempt in range(1, GEMINI_MAX_RETRIES + 2):  # +2: first try + N retries
            try:
                return await asyncio.to_thread(chat.send_message, content)
            except genai_errors.ServerError as e:
                if attempt > GEMINI_MAX_RETRIES:
                    raise
                log.warning(
                    "Gemini server error (attempt %d/%d), retrying in %ds: %s",
                    attempt, GEMINI_MAX_RETRIES + 1, GEMINI_RETRY_BACKOFF_SECONDS, e,
                )
                await asyncio.sleep(GEMINI_RETRY_BACKOFF_SECONDS)
            except genai_errors.ClientError as e:
                # Only 429 is worth retrying -- 400/403/404 etc. are our bug
                # or a bad config and will fail identically every time.
                if getattr(e, "code", None) != 429:
                    raise
                delay = _retry_delay_seconds(e)
                out_of_attempts = attempt > GEMINI_MAX_RETRIES
                too_long = delay is None or delay > GEMINI_MAX_QUOTA_WAIT_SECONDS
                if out_of_attempts or too_long:
                    log.error("Gemini quota exhausted (suggested wait: %ss): %s", delay, e)
                    raise QuotaExceededError(str(e)) from e
                log.warning(
                    "Gemini quota hit (attempt %d/%d), waiting %.1fs as instructed by the API",
                    attempt, GEMINI_MAX_RETRIES + 1, delay,
                )
                await asyncio.sleep(delay + 0.5)  # small cushion past the window

    async def ask(self, session_id: str, message: str) -> str:
        """Send a user message, resolving any MCP tool calls Gemini makes
        along the way, and return the final text reply."""
        chat = self._get_chat(session_id)
        response = await self._send_message(chat, message)

        # Gemini may chain multiple tool calls before it's ready to answer.
        while response.function_calls:
            function_response_parts = []
            for call in response.function_calls:
                log.info("Gemini -> MCP tool call: %s(%s)", call.name, dict(call.args or {}))
                try:
                    result = await asyncio.wait_for(
                        self.mcp_session.call_tool(call.name, dict(call.args or {})),
                        timeout=MCP_TOOL_TIMEOUT_SECONDS,
                    )
                    result_text = _tool_result_to_text(result)
                except (McpError, asyncio.TimeoutError) as e:
                    log.error("MCP tool call %s timed out or failed: %s", call.name, e)
                    result_text = (
                        "(this tool call failed or timed out -- tell the user the "
                        "knowledge base is temporarily unavailable and to try again "
                        "in a moment)"
                    )
                function_response_parts.append(
                    types.Part.from_function_response(
                        name=call.name, response={"result": result_text}
                    )
                )
            response = await self._send_message(chat, function_response_parts)

        return response.text or "I couldn't come up with an answer for that."


def _tool_result_to_text(result) -> str:
    """MCP tool results are a list of content blocks (text/image/etc). We
    only care about text for this bot."""
    parts = []
    for block in result.content:
        text = getattr(block, "text", None)
        if text:
            parts.append(text)
    return "\n".join(parts) if parts else "(no results)"
