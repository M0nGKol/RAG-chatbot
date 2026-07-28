"""One-off schema setup. Runs schema/init_schema.cypher over the Bolt driver,
so it works against any Neo4j deployment (Aura, Docker, Desktop) without
needing shell/cypher-shell access -- handy for Aura Free, where you can't
docker exec into anything.

    python -m scripts.init_db
"""
from __future__ import annotations

import re
from pathlib import Path

from neo4j import GraphDatabase

from common.config import load_settings

SCHEMA_FILE = Path(__file__).resolve().parent.parent / "schema" / "init_schema.cypher"


def _statements(cypher_text: str) -> list[str]:
    no_comments = re.sub(r"//.*", "", cypher_text)
    return [s.strip() for s in no_comments.split(";") if s.strip()]


def main() -> None:
    settings = load_settings()
    driver = GraphDatabase.driver(
        settings.neo4j_uri, auth=(settings.neo4j_username, settings.neo4j_password)
    )
    statements = _statements(SCHEMA_FILE.read_text())

    with driver.session(database=settings.neo4j_database) as session:
        for i, stmt in enumerate(statements, 1):
            first_line = stmt.splitlines()[0][:80]
            print(f"[{i}/{len(statements)}] {first_line}...")
            session.run(stmt)

    driver.close()
    print("Schema setup complete: constraints + vector indexes are live.")


if __name__ == "__main__":
    main()
