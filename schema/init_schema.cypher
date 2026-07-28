// ---------------------------------------------------------------------------
// Knowledge graph schema for the RAG Telegram bot.
//
// Nodes:
//   (:Concept {name, summary, embedding, created_at, updated_at})
//   (:Chunk   {text, embedding, source, created_at})
//
// Relationships:
//   (:Chunk)-[:ABOUT]->(:Concept)          chunk belongs to a concept
//   (:Concept)-[:RELATED_TO]->(:Concept)   concept-to-concept graph links
//
// Run once against a fresh database, e.g.:
//   cat schema/init_schema.cypher | cypher-shell -u neo4j -p <password>
// ---------------------------------------------------------------------------

CREATE CONSTRAINT concept_name_unique IF NOT EXISTS
FOR (c:Concept) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT chunk_id_unique IF NOT EXISTS
FOR (c:Chunk) REQUIRE c.id IS UNIQUE;

// Native Neo4j vector indexes (Neo4j 5.13+). Dimensions must match
// EMBEDDING_DIMENSIONS in your .env (default 768, truncated via Gemini's
// output_dimensionality / Matryoshka support).
CREATE VECTOR INDEX chunk_embeddings IF NOT EXISTS
FOR (c:Chunk) ON (c.embedding)
OPTIONS {
  indexConfig: {
    `vector.dimensions`: 768,
    `vector.similarity_function`: 'cosine'
  }
};

CREATE VECTOR INDEX concept_embeddings IF NOT EXISTS
FOR (c:Concept) ON (c.embedding)
OPTIONS {
  indexConfig: {
    `vector.dimensions`: 768,
    `vector.similarity_function`: 'cosine'
  }
};
