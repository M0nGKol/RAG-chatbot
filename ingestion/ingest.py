"""CLI entrypoint for feeding new documents into the knowledge graph.

Usage:
    # single file
    python -m ingestion.ingest --file path/to/doc.md --source "doc.md"

    # every .md in a folder (looks for a same-name .json sidecar next to
    # each file for a nicer --source label, e.g. from data/extracted/)
    python -m ingestion.ingest --dir data/extracted --pattern "*.md"

Only plain text formats (.md/.txt) are supported -- there is no PDF parser
in this pipeline. If you're starting from PDFs, extract them to markdown
first (this repo assumes that's already been done, see data/extracted/).

For every chunk in a file:
  1. Embed it with Gemini.
  2. Vector-search Neo4j for the closest existing chunk.
  3. SKIP / EXTEND / NEW per ingestion/dedup.py, and write to Neo4j accordingly.

Run this whenever you have new material to add -- it's idempotent-ish by
design: re-running it on content you've already ingested should mostly
produce SKIPs, not duplicate nodes.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from common.config import load_settings
from common.gemini_client import GeminiClient
from common.neo4j_client import Neo4jClient
from ingestion.chunking import chunk_text
from ingestion.dedup import Action, decide, decide_within_concept

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("ingest")


def _load_sidecar(path: Path) -> dict | None:
    sidecar = path.with_suffix(".json")
    if not sidecar.exists():
        return None
    try:
        return json.loads(sidecar.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _source_label(path: Path, meta: dict | None) -> str:
    """Prefer a same-name .json sidecar (doc_id/course/week/title/source_type)
    for a readable source label; fall back to the filename."""
    if not meta:
        return path.name

    course = meta.get("course")
    week = meta.get("week")
    title = meta.get("title", path.stem)
    source_type = meta.get("source_type")

    label = title
    if course and week is not None:
        label = f"{course} W{week} - {label}"
    if source_type:
        label = f"{label} ({source_type})"
    return label


def _concept_label(meta: dict | None) -> str | None:
    """Deterministic concept name from metadata (course + title), so topic
    boundaries come from how you organized your files, not from an
    embedding-similarity guess. Returns None if there's no sidecar -- caller
    falls back to embedding-driven topic discovery in that case."""
    if not meta or not meta.get("title"):
        return None
    course = meta.get("course")
    title = meta["title"]
    return f"{course} - {title}" if course else title


def ingest_file(path: Path, source: str, gemini: GeminiClient, neo4j: Neo4jClient, meta: dict | None) -> dict:
    text = path.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    log.info("Split %s into %d chunk(s)", path, len(chunks))

    stats = {Action.SKIP: 0, Action.EXTEND: 0, Action.NEW: 0}
    forced_concept = _concept_label(meta)

    if forced_concept and not neo4j.concept_exists(forced_concept):
        summary_source = text[:4000]
        labeled = gemini.summarize_concept(summary_source)
        neo4j.upsert_concept(
            name=forced_concept,
            summary=labeled.get("summary", meta.get("title", forced_concept)),
            embedding=gemini.embed_text(forced_concept, task_type="RETRIEVAL_DOCUMENT"),
        )
        log.info("Created concept '%s' from document metadata", forced_concept)

    for i, chunk in enumerate(chunks):
        embedding = gemini.embed_text(chunk, task_type="RETRIEVAL_DOCUMENT")

        if forced_concept:
            decision = decide_within_concept(embedding, neo4j, gemini.settings, forced_concept)
        else:
            decision = decide(embedding, neo4j, gemini.settings)
        stats[decision.action] += 1

        if decision.action == Action.SKIP:
            log.info(
                "[%d/%d] SKIP (score=%.3f, already covered by concept '%s')",
                i + 1, len(chunks), decision.best_score, decision.best_match_concept,
            )
            continue

        if decision.action == Action.EXTEND:
            concept_name = decision.best_match_concept
            log.info(
                "[%d/%d] EXTEND concept '%s' (score=%.3f)",
                i + 1, len(chunks), concept_name, decision.best_score,
            )
        elif forced_concept:
            concept_name = forced_concept
            log.info(
                "[%d/%d] ADD to concept '%s' (best prior score=%.3f)",
                i + 1, len(chunks), concept_name, decision.best_score,
            )
        else:  # NEW, topic-discovery path
            labeled = gemini.summarize_concept(chunk)
            concept_name = labeled["name"]
            neo4j.upsert_concept(
                name=concept_name,
                summary=labeled["summary"],
                embedding=gemini.embed_text(labeled["summary"], task_type="RETRIEVAL_DOCUMENT"),
            )
            log.info(
                "[%d/%d] NEW concept '%s' (best prior score=%.3f)",
                i + 1, len(chunks), concept_name, decision.best_score,
            )
            if decision.best_match_concept:
                neo4j.link_concepts(concept_name, decision.best_match_concept)

        neo4j.add_chunk(
            text=chunk, source=source, embedding=embedding, concept_name=concept_name
        )

    log.info(
        "Done with %s. skipped=%d extended=%d new=%d",
        path.name, stats[Action.SKIP], stats[Action.EXTEND], stats[Action.NEW],
    )
    return stats


def ingest_paths(paths: list[Path], source_override: str | None = None) -> None:
    settings = load_settings()
    gemini = GeminiClient(settings)
    neo4j = Neo4jClient(settings)

    totals = {Action.SKIP: 0, Action.EXTEND: 0, Action.NEW: 0}
    try:
        for path in paths:
            meta = _load_sidecar(path)
            source = source_override or _source_label(path, meta)
            stats = ingest_file(path, source, gemini, neo4j, meta)
            for action, count in stats.items():
                totals[action] += count
    finally:
        neo4j.close()

    log.info(
        "All done (%d file(s)). skipped=%d extended=%d new=%d",
        len(paths), totals[Action.SKIP], totals[Action.EXTEND], totals[Action.NEW],
    )


def main():
    parser = argparse.ArgumentParser(description="Ingest document(s) into the knowledge graph.")
    parser.add_argument("--file", type=Path, help="Path to a single .md/.txt file")
    parser.add_argument("--dir", type=Path, help="Folder to ingest every matching file from")
    parser.add_argument("--pattern", default="*.md", help="Glob pattern used with --dir (default: *.md)")
    parser.add_argument(
        "--source", default=None,
        help="Override the source label for all ingested files (default: derived per-file from a .json sidecar, or the filename)",
    )
    args = parser.parse_args()

    if not args.file and not args.dir:
        parser.error("pass either --file or --dir")

    if args.file:
        if not args.file.exists():
            log.error("File not found: %s", args.file)
            sys.exit(1)
        ingest_paths([args.file], args.source)
        return

    if not args.dir.exists():
        log.error("Directory not found: %s", args.dir)
        sys.exit(1)
    files = sorted(args.dir.glob(args.pattern))
    if not files:
        log.error("No files matching %s in %s", args.pattern, args.dir)
        sys.exit(1)
    log.info("Found %d file(s) to ingest from %s", len(files), args.dir)
    ingest_paths(files, args.source)


if __name__ == "__main__":
    main()
