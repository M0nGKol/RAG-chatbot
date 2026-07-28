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

import logging
import os
from contextlib import AsyncExitStack

from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from common.config import Settings
from orchestrator.schema_convert import json_schema_to_genai_schema

log = logging.getLogger("orchestrator")

SYSTEM_INSTRUCTION = """You are a helpful assistant answering questions using \
a Neo4j knowledge graph as your source of truth. You have tools available to \
search and query that graph -- use them before answering any question that \
depends on the knowledge base rather than guessing. If the tools return \
nothing relevant, say plainly that you don't have that information yet \
instead of making something up. Keep answers concise and suited for a \
Telegram chat."""


class GraphRAGOrchestrator:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.genai_client = genai.Client(api_key=settings.google_api_key)
        self._stack = AsyncExitStack()
        self.mcp_session: ClientSession | None = None
        self._gemini_tool: types.Tool | None = None
        self._chats: dict[str, "genai.chats.Chat"] = {}

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

    async def stop(self) -> None:
        await self._stack.aclose()

    def _get_chat(self, session_id: str):
        if session_id not in self._chats:
            self._chats[session_id] = self.genai_client.chats.create(
                model=self.settings.gemini_model,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    tools=[self._gemini_tool],
                ),
            )
        return self._chats[session_id]

    async def ask(self, session_id: str, message: str) -> str:
        """Send a user message, resolving any MCP tool calls Gemini makes
        along the way, and return the final text reply."""
        chat = self._get_chat(session_id)
        response = chat.send_message(message)

        # Gemini may chain multiple tool calls before it's ready to answer.
        while response.function_calls:
            function_response_parts = []
            for call in response.function_calls:
                log.info("Gemini -> MCP tool call: %s(%s)", call.name, dict(call.args or {}))
                result = await self.mcp_session.call_tool(call.name, dict(call.args or {}))
                result_text = _tool_result_to_text(result)
                function_response_parts.append(
                    types.Part.from_function_response(
                        name=call.name, response={"result": result_text}
                    )
                )
            response = chat.send_message(function_response_parts)

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
