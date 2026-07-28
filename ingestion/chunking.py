"""Minimal paragraph-aware chunker. Swap for something smarter (token-aware,
recursive splitter, etc.) if your documents need it -- this is intentionally
simple so the dedup logic is easy to follow."""
from __future__ import annotations


def chunk_text(text: str, max_chars: int = 1200) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    buffer = ""

    for para in paragraphs:
        if len(buffer) + len(para) + 2 <= max_chars:
            buffer = f"{buffer}\n\n{para}" if buffer else para
        else:
            if buffer:
                chunks.append(buffer)
            buffer = para

    if buffer:
        chunks.append(buffer)

    return chunks
