"""Standalone MCP connectivity check -- confirms the Neo4j MCP server can be
launched, connects to your Aura instance, and exposes tools to Gemini,
without needing to run the full Telegram bot.

    python -m scripts.check_mcp
    python -m scripts.check_mcp --ask "What topics do you know about?"
"""
from __future__ import annotations

import argparse
import asyncio
import logging

from common.config import load_settings
from orchestrator.gemini_mcp_bridge import GraphRAGOrchestrator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("check_mcp")


async def run(ask: str | None) -> None:
    settings = load_settings()
    log.info("MCP server command: %s", settings.mcp_server_command)
    log.info("Neo4j URI: %s", settings.neo4j_uri)

    orchestrator = GraphRAGOrchestrator(settings)
    try:
        log.info("Launching MCP server and connecting to Neo4j...")
        await orchestrator.start()
        log.info("Connected. MCP server is set up correctly.")

        if ask:
            log.info("Asking Gemini (will call MCP tools as needed): %r", ask)
            answer = await orchestrator.ask("check-mcp", ask)
            print("\n--- Gemini's answer ---")
            print(answer)
    finally:
        await orchestrator.stop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Check the Neo4j MCP server is reachable.")
    parser.add_argument("--ask", default=None, help="Also send a test question through Gemini + MCP")
    args = parser.parse_args()
    asyncio.run(run(args.ask))


if __name__ == "__main__":
    main()
