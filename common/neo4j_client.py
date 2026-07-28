"""Direct Neo4j driver access used ONLY by the ingestion pipeline.

The chat path never touches this file — at query time Gemini reaches Neo4j
exclusively through the MCP server (see orchestrator/gemini_mcp_bridge.py),
so the LLM can only run the read/write operations the MCP server chooses to
expose. Ingestion is a controlled, non-LLM-driven process, so it's fine (and
faster) for it to talk to the driver directly.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone

from neo4j import GraphDatabase

from common.config import Settings


class Neo4jClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.driver = GraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_username, settings.neo4j_password),
        )

    def close(self):
        self.driver.close()

    def _session(self):
        return self.driver.session(database=self.settings.neo4j_database)

    # ---- similarity search -------------------------------------------------

    def vector_search_chunks(self, embedding: list[float], top_k: int):
        """Global search across every chunk in the graph, regardless of which
        concept it belongs to. Used only as the topic-discovery fallback for
        content with no metadata sidecar -- see ingestion/dedup.decide()."""
        query = """
        CALL db.index.vector.queryNodes('chunk_embeddings', $top_k, $embedding)
        YIELD node, score
        OPTIONAL MATCH (node)-[:ABOUT]->(concept:Concept)
        RETURN node.id AS chunk_id, node.text AS text, node.source AS source,
               score, concept.name AS concept_name
        ORDER BY score DESC
        """
        with self._session() as session:
            result = session.run(query, embedding=embedding, top_k=top_k)
            return [record.data() for record in result]

    def vector_search_chunks_in_concept(self, embedding: list[float], concept_name: str, top_k: int):
        """Search only among chunks already attached to a specific concept.
        Used when the concept is already known (from document metadata) and
        we just need to know "is this exact content already in there?" --
        much more reliable than comparing against the whole graph, since it
        can't be confused by unrelated topics that merely share vocabulary."""
        query = """
        CALL db.index.vector.queryNodes('chunk_embeddings', $top_k, $embedding)
        YIELD node, score
        MATCH (node)-[:ABOUT]->(concept:Concept {name: $concept_name})
        RETURN node.id AS chunk_id, node.text AS text, node.source AS source,
               score, concept.name AS concept_name
        ORDER BY score DESC
        """
        with self._session() as session:
            result = session.run(
                query, embedding=embedding, concept_name=concept_name, top_k=top_k
            )
            return [record.data() for record in result]

    def concept_exists(self, name: str) -> bool:
        query = "MATCH (c:Concept {name: $name}) RETURN count(c) > 0 AS exists"
        with self._session() as session:
            return session.run(query, name=name).single()["exists"]

    # ---- writes --------------------------------------------------------------

    def upsert_concept(self, name: str, summary: str, embedding: list[float]) -> str:
        query = """
        MERGE (c:Concept {name: $name})
        ON CREATE SET c.summary = $summary,
                       c.embedding = $embedding,
                       c.created_at = $now
        ON MATCH SET  c.updated_at = $now
        RETURN c.name AS name
        """
        now = datetime.now(timezone.utc).isoformat()
        with self._session() as session:
            result = session.run(
                query, name=name, summary=summary, embedding=embedding, now=now
            )
            return result.single()["name"]

    def add_chunk(self, text: str, source: str, embedding: list[float], concept_name: str) -> str:
        chunk_id = str(uuid.uuid4())
        query = """
        MATCH (concept:Concept {name: $concept_name})
        CREATE (chunk:Chunk {
            id: $chunk_id, text: $text, source: $source,
            embedding: $embedding, created_at: $now
        })
        CREATE (chunk)-[:ABOUT]->(concept)
        RETURN chunk.id AS id
        """
        now = datetime.now(timezone.utc).isoformat()
        with self._session() as session:
            result = session.run(
                query,
                concept_name=concept_name,
                chunk_id=chunk_id,
                text=text,
                source=source,
                embedding=embedding,
                now=now,
            )
            return result.single()["id"]

    def link_concepts(self, name_a: str, name_b: str, relationship: str = "RELATED_TO"):
        query = f"""
        MATCH (a:Concept {{name: $name_a}}), (b:Concept {{name: $name_b}})
        MERGE (a)-[:{relationship}]->(b)
        """
        with self._session() as session:
            session.run(query, name_a=name_a, name_b=name_b)
