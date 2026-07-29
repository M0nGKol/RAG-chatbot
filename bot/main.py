"""Entrypoint: starts the MCP session against Neo4j, then runs the Telegram
bot in polling mode.

    python -m bot.main
"""
from __future__ import annotations

import asyncio
import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.telegram_bot import handle_message, start_command
from common.config import load_settings
from orchestrator.gemini_mcp_bridge import GraphRAGOrchestrator

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("main")


async def run() -> None:
    settings = load_settings()

    orchestrator = GraphRAGOrchestrator(settings)
    await orchestrator.start()
    log.info("Connected to Neo4j MCP server.")

    # concurrent_updates: without this, python-telegram-bot processes one
    # update at a time -- with a whole batch/class using this bot, that
    # means everyone queues up behind whoever asked first, even once a
    # single request can no longer freeze the process outright. A modest
    # cap (rather than unlimited) keeps a burst of messages from all
    # hammering the Gemini/MCP/Aura calls at once.
    application = (
        Application.builder()
        .token(settings.telegram_bot_token)
        .concurrent_updates(8)
        .build()
    )
    application.bot_data["orchestrator"] = orchestrator
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    try:
        async with application:
            await application.start()
            await application.updater.start_polling()
            log.info("Bot is polling. Press Ctrl+C to stop.")
            await asyncio.Event().wait()  # run forever
    finally:
        await application.updater.stop()
        await application.stop()
        await orchestrator.stop()


if __name__ == "__main__":
    asyncio.run(run())
