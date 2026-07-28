I built a RAG chatbot for my Operations Research batch's exam prep — and spent most of the effort making sure it actually learns, instead of just regurgitating whatever gets uploaded to it.

The setup:

A Telegram bot, backed by Google Gemini (via Google AI Studio) as the reasoning layer. The knowledge base isn't a flat vector store — it's a Neo4j graph, with Concept nodes (Introduction, Linear Programming, Simplex Method, Duality, Transportation Model, Assignment Problem, and so on) and Chunk nodes attached to them. Gemini never talks to Neo4j directly. It reaches the graph through an MCP (Model Context Protocol) server, calling schema-inspection and query tools at answer time rather than holding a database connection itself.

The part I cared most about: incremental learning.

Every time new course material comes in, each chunk gets embedded and checked against what's already in its topic. If it's a near-duplicate of something already there, it's skipped — no bloat from re-uploading the same slides twice. If it's new detail on a topic that already exists, it's added to that concept. If it's a genuinely new topic, it becomes a new concept node in the graph. So the knowledge base only grows with actual information, and re-running ingestion on the same material is a no-op rather than a mess of duplicates.

Getting the dedup boundary right was trickier than I expected — my first pass compared new content against the entire graph by embedding similarity alone, and it turned out that ten weeks of the same course share enough vocabulary that genuinely different topics scored 90%+ "similar" to each other. Fixed it by making concept assignment deterministic from document metadata and scoping duplicate-detection to within a topic, not across the whole graph.

Stack: Python, Neo4j Aura, Google Gemini, MCP, python-telegram-bot. Containerized with Docker, deployed as a background worker.

Built for my batch, but the pattern — LLM + graph-structured knowledge base + MCP as the connective layer, with real incremental-learning semantics on ingestion — is one I'd reach for again for any domain-specific study or documentation assistant.

#RAG #Neo4j #GraphDatabase #GoogleGemini #ModelContextProtocol #GenAI #Python #OperationsResearch
