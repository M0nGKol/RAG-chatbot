"""The "only learn new/extra knowledge" logic.

Two modes, picked per-file by ingestion/ingest.py:

1. Metadata-driven (preferred, used whenever a file has a .json sidecar with
   course/week/title -- e.g. data/extracted/). The concept is decided
   deterministically from that metadata, NOT from embedding similarity, so
   "Linear Programming" and "Duality" always land in their own concepts even
   though they share a lot of domain vocabulary. decide_within_concept() then
   only answers one narrower question: is this chunk's text already present
   in THAT concept? That's a much easier, more reliable comparison than
   guessing topic boundaries from raw cosine similarity.

2. Topic-discovery fallback (used for files with no metadata). decide()
   compares a new chunk against every existing chunk in the whole graph and
   picks SKIP / EXTEND / NEW by threshold. This is inherently fuzzier --
   domain-specific text (e.g. a whole course on one subject) can score
   0.90+ similarity across genuinely different topics, so don't be surprised
   if it needs threshold tuning for your content. Prefer adding a metadata
   sidecar over relying on this path when you can.

Thresholds are cosine similarity (0-1) and live in .env.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from common.config import Settings
from common.neo4j_client import Neo4jClient

# How many same-concept candidates to pull back before filtering. Needs to be
# generous (not settings.top_k_similar) because the underlying vector index
# query returns its top-K across the WHOLE graph before we filter down to a
# single concept -- too small a K here and a real duplicate in a big concept
# could get missed just because other concepts' chunks crowded it out of the
# global top-K.
_WITHIN_CONCEPT_SEARCH_K = 50


class Action(str, Enum):
    SKIP = "skip"
    EXTEND = "extend"
    NEW = "new"


@dataclass
class Decision:
    action: Action
    best_score: float
    best_match_chunk_id: str | None
    best_match_concept: str | None


def decide(embedding: list[float], neo4j: Neo4jClient, settings: Settings) -> Decision:
    """Topic-discovery fallback for files with no metadata sidecar."""
    matches = neo4j.vector_search_chunks(embedding, settings.top_k_similar)

    if not matches:
        return Decision(Action.NEW, 0.0, None, None)

    top = matches[0]
    score = top["score"]

    if score >= settings.duplicate_threshold:
        action = Action.SKIP
    elif score >= settings.extend_threshold:
        action = Action.EXTEND
    else:
        action = Action.NEW

    return Decision(
        action=action,
        best_score=score,
        best_match_chunk_id=top["chunk_id"],
        best_match_concept=top["concept_name"],
    )


def decide_within_concept(
    embedding: list[float], neo4j: Neo4jClient, settings: Settings, concept_name: str
) -> Decision:
    """Metadata-driven path: concept is already fixed, so this only decides
    SKIP (near-duplicate of a chunk already in this concept) vs NEW (write
    it). Never returns EXTEND -- there's nothing to "extend into", the
    concept was already chosen from the document's own metadata."""
    matches = neo4j.vector_search_chunks_in_concept(
        embedding, concept_name, _WITHIN_CONCEPT_SEARCH_K
    )

    if not matches:
        return Decision(Action.NEW, 0.0, None, concept_name)

    top = matches[0]
    score = top["score"]
    action = Action.SKIP if score >= settings.duplicate_threshold else Action.NEW

    return Decision(
        action=action,
        best_score=score,
        best_match_chunk_id=top["chunk_id"],
        best_match_concept=concept_name,
    )
