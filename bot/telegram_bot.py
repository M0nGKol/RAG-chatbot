"""Telegram handlers. Kept separate from main.py so the wiring (which
orchestrator instance, which settings) stays in one place."""
from __future__ import annotations

import logging
import telegramify_markdown
from telegram import Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from orchestrator.gemini_mcp_bridge import GraphRAGOrchestrator, QuotaExceededError

log = logging.getLogger("telegram_bot")

async def _reply_formatted(message, text: str) -> None:
    """Gemini replies in standard Markdown (**bold**, "* " bullets, etc.),
    which isn't the same dialect Telegram renders. Convert to Telegram's
    MarkdownV2 (bold, bullet glyphs, escaped punctuation) before sending. If
    the converted text still trips Telegram's stricter parser on some edge
    case, fall back to plain text rather than erroring out the reply."""
    try:
        formatted = telegramify_markdown.markdownify(text)
        await message.reply_text(formatted, parse_mode=ParseMode.MARKDOWN_V2)
    except BadRequest:
        log.warning("MarkdownV2 send failed, falling back to plain text", exc_info=True)
        await message.reply_text(text)
        
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _reply_formatted(
        update.message,
        "Hi! Ask me anything -- I'll look it up in the knowledge graph before answering. "
        "Currently I can help you with information from our knowledge base. The context "
        "of our knowledge base only covers OR lessons 1 to 11. I will add more soon.",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    orchestrator: GraphRAGOrchestrator = context.bot_data["orchestrator"]
    session_id = str(update.effective_chat.id)
    user_text = update.message.text

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        reply = await orchestrator.ask(session_id, user_text)
    except QuotaExceededError:
        log.error("Gemini quota exhausted while answering %s", session_id)
        reply = (
            "I've hit my AI usage limit for now, so I can't answer this one. "
            "This resets after a short wait (or at the start of the next day "
            "if the daily cap is reached) -- please try again later."
        )
    except Exception:
        log.exception("Error handling message from %s", session_id)
        reply = "Something went wrong on my end -- please try again in a moment."

    await _reply_formatted(update.message, reply)
