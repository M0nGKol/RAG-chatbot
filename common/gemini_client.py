"""Thin wrapper around the google-genai SDK for embeddings + concept naming.

Chat generation itself is handled by orchestrator/gemini_mcp_bridge.py (it
needs the raw genai client to do function-calling against MCP tools). This
module only covers the two things the ingestion pipeline needs:
  1. embed_text()      -> vector for a chunk / query
  2. summarize_concept() -> short name + summary for a brand-new topic
"""
from __future__ import annotations

from google import genai
from google.genai import types

from common.config import Settings

# Ingestion is a synchronous CLI script (no event loop to block), but a
# request-level timeout still matters so a stuck network call doesn't hang
# the whole ingestion run forever.
GEMINI_REQUEST_TIMEOUT_MS = 30_000


class GeminiClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = genai.Client(
            api_key=settings.google_api_key,
            http_options=types.HttpOptions(timeout=GEMINI_REQUEST_TIMEOUT_MS),
        )

    def embed_text(self, text: str, task_type: str = "RETRIEVAL_DOCUMENT") -> list[float]:
        """Embed a single string. task_type should be RETRIEVAL_DOCUMENT for
        ingested content and RETRIEVAL_QUERY for user questions."""
        result = self.client.models.embed_content(
            model=self.settings.gemini_embedding_model,
            contents=text,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=self.settings.embedding_dimensions,
            ),
        )
        return result.embeddings[0].values

    def summarize_concept(self, text: str) -> dict:
        """Ask Gemini for a short canonical concept name + one-line summary
        for a chunk that didn't match anything existing in the graph. Used
        when the ingestion pipeline decides a chunk is a genuinely new topic.
        """
        prompt = (
            "You are labeling a knowledge graph. Read the passage below and "
            "return a short canonical concept name (2-5 words, Title Case) "
            "and a one-sentence summary. Respond as strict JSON with keys "
            '"name" and "summary", nothing else.\n\n'
            f"Passage:\n{text[:4000]}"
        )
        response = self.client.models.generate_content(
            model=self.settings.gemini_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        import json

        return json.loads(response.text)
