# RAG Telegram Bot — Neo4j + MCP + Gemini

Telegram bot that answers from a Neo4j knowledge graph. Gemini (Google AI
Studio) is the LLM; it never touches Neo4j directly — it reaches the graph
only through a Neo4j MCP server's tools. A separate ingestion pipeline adds
new documents to the graph, skipping content that's already known and only
writing genuinely new or additional information.

```
Telegram user
    -> bot/main.py (python-telegram-bot)
    -> orchestrator/gemini_mcp_bridge.py (Gemini function-calling loop)
    -> Neo4j MCP server (subprocess, stdio)
    -> Neo4j Aura (graph + native vector index)

Document
    -> ingestion/ingest.py (chunk -> embed -> dedup check -> write)
    -> Neo4j Aura
```

## 1. Prerequisites

- Python 3.11+
- A Neo4j Aura account (free, no credit card): https://console.neo4j.io
- A Google AI Studio API key: https://aistudio.google.com/apikey
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## 2. Create your Neo4j Aura instance

1. Go to https://console.neo4j.io and sign up / log in.
2. Click **New Instance** -> choose **AuraDB Free**.
3. Give it a name (e.g. `rag-kb`) and create it.
4. Aura shows you a credentials screen **once** with the connection URI,
   username (`neo4j`), and a generated password. Download the credentials
   file or copy them now — the password is not retrievable later (you'd
   have to reset it).
5. Wait ~1-2 minutes for the instance status to become **Running**.

Free tier notes: single database, ~200K nodes / 400K relationships depending
on current Aura limits, native vector indexes are supported. Plenty for a
personal knowledge base; if you outgrow it, upgrade the instance later
without changing any code here.

## 3. Configure the project

```bash
cd rag-neo4j-telegram-bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
```

Edit `.env`:
- `NEO4J_URI` — the `neo4j+s://xxxxxxxx.databases.neo4j.io` URI from Aura
- `NEO4J_USERNAME` / `NEO4J_PASSWORD` — from the credentials screen
- `TELEGRAM_BOT_TOKEN` — from BotFather
- `GOOGLE_API_KEY` — from Google AI Studio

Install the Neo4j MCP server (this is what `MCP_SERVER_COMMAND` launches):

```bash
pip install neo4j-mcp-server
# or, for the Cypher-focused Neo4j Labs server instead:
# pip install mcp-neo4j-cypher
```

## 4. Create the schema

Aura Free has no shell access to `docker exec`/`cypher-shell` into, so use
the included Python script — it runs `schema/init_schema.cypher` straight
over the Bolt driver using the credentials in `.env`:

```bash
python -m scripts.init_db
```

This creates the `Concept`/`Chunk` uniqueness constraints and the two
native vector indexes (`chunk_embeddings`, `concept_embeddings`) that
ingestion and retrieval both rely on. You can also paste the contents of
`schema/init_schema.cypher` into the **Query** tab in the Aura Console if
you'd rather run it there and watch it execute.

## 5. Ingest some knowledge

Only plain text (`.md`/`.txt`) goes in — there's no PDF parser in this
pipeline. If you're starting from PDFs, extract them to markdown first
(e.g. `data/raw/*.pdf` -> `data/extracted/*.md`, one optional same-name
`.json` sidecar per file with `course`/`week`/`title`/`source_type` for a
nicer source label).

Single file:
```bash
python -m ingestion.ingest --file path/to/doc.md --source "doc"
```

Whole folder at once (this is what you want for `data/extracted/`):
```bash
python -m ingestion.ingest --dir data/extracted --pattern "*.md"
```
Without `--source`, each file's label is pulled from its `.json` sidecar
(e.g. `OR1 W1 - Introduction (slides)`) or falls back to the filename.

**How concepts get assigned:** if a file has a `.json` sidecar with
`course`/`title`, the concept name is taken straight from that metadata
(e.g. `"OR1 - Linear Programming"`) — deterministic, not guessed. Dedup then
only asks one question per chunk: is this text already present in *that*
concept? `DUPLICATE_THRESHOLD` controls that. Files with no sidecar fall
back to comparing against the whole graph and picking SKIP/EXTEND/NEW by
threshold — looser, and more likely to need tuning, since domain-specific
text can score deceptively high similarity across genuinely different
topics. Prefer adding a sidecar over relying on that fallback.

Run ingestion again on the same file (or a file with overlapping content)
and you should see mostly `SKIP` — that's the "don't relearn, only add"
behavior. If real new info is getting skipped, raise `DUPLICATE_THRESHOLD`
in `.env`.

You can sanity-check what landed in the graph from the Aura Console's
**Query** tab, e.g. `MATCH (c:Concept) RETURN c.name, c.summary` or
`MATCH (c:Concept)<-[:ABOUT]-(chunk:Chunk) RETURN c.name, count(chunk)`.

## 6. Check the MCP server before running the bot

The MCP server (`neo4j-mcp-server`, installed in step 3) is what lets Gemini
query your Aura instance at chat time. Confirm it actually launches and
connects before wiring up Telegram:

```bash
python -m scripts.check_mcp
```

You should see `Connected. MCP server is set up correctly.` and a log line
listing the tools it exposes (schema inspection, Cypher execution, etc).
To also test the full Gemini -> MCP -> Neo4j round trip:

```bash
python -m scripts.check_mcp --ask "What topics do you know about?"
```

If this fails, it's almost always one of: `NEO4J_URI`/`NEO4J_USERNAME`/
`NEO4J_PASSWORD` wrong in `.env`, the Aura instance not in **Running**
state, or `neo4j-mcp-server` not installed (`pip install neo4j-mcp-server`).

## 7. Run the bot

```bash
python -m bot.main
```

This starts the same MCP connection as step 6, then begins polling
Telegram. Message your bot — each reply goes through Gemini, which calls
the Neo4j MCP server's tools as needed before answering. Leave this process
running (see "Keeping it running" below) for the bot to keep responding.

## Deploying to Render (Docker)

`python -m bot.main` uses long-polling, so nothing needs to be publicly
reachable — it just needs to run continuously. This repo includes a
`Dockerfile` and `render.yaml` for that.

**Prerequisite:** push this repo to GitHub (Render deploys from a repo, not
a local folder).

1. In the Render dashboard: **New +** → **Background Worker** (not "Web
   Service" — this app has no HTTP server, and a Web Service on Render
   expects one and will be marked unhealthy).
2. Connect your GitHub repo. Render will detect the `Dockerfile`
   automatically and select the Docker runtime — leave build/start commands
   blank, the `Dockerfile`'s `CMD` handles that.
3. Pick a plan. **Background workers have no free tier on Render** — you
   need at least the Starter plan (~$7/mo) for this service.
4. Under **Environment**, add every value from your local `.env` as an
   environment variable: `TELEGRAM_BOT_TOKEN`, `GOOGLE_API_KEY`,
   `GEMINI_MODEL`, `GEMINI_EMBEDDING_MODEL`, `EMBEDDING_DIMENSIONS`,
   `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`,
   `MCP_SERVER_COMMAND=neo4j-mcp-server`, `DUPLICATE_THRESHOLD`,
   `EXTEND_THRESHOLD`, `TOP_K_SIMILAR`. Nothing in `.env` gets committed or
   read from the repo — Render only sees what you put in this dashboard.
5. Deploy. Check the **Logs** tab for `Connected. MCP server is set up
   correctly.` (from `orchestrator.start()`) and then Telegram polling
   starting — that confirms it's live.

Alternative: `render.yaml` in this repo is a Blueprint you can use instead
of the manual steps above (**New +** → **Blueprint**, point it at the
repo) — it declares the same service and env var names, you just fill in
the secret values when prompted. Render's blueprint schema does evolve, so
if it fails to parse, fall back to the manual dashboard flow, which doesn't
depend on this file at all.

`neo4j-mcp-server` isn't deployed or run separately — it's a normal Python
dependency now (in `requirements.txt`) that gets installed into the image
and launched as a subprocess by the bot itself (see
`orchestrator/gemini_mcp_bridge.py`); it starts and stops with the worker
process.

**Local Docker testing**, before pushing to Render, if you want to sanity
check the image builds and runs:
```bash
docker build -t rag-bot .
docker run --env-file .env rag-bot
```

## Project layout

```
common/            shared config, Neo4j driver wrapper, Gemini embedding client
ingestion/         chunking + dedup + the ingest CLI
orchestrator/       Gemini <-> MCP bridge (tool discovery, call loop)
bot/               Telegram handlers + entrypoint
schema/            Cypher schema (vector indexes, constraints)
scripts/           one-off ops scripts (schema init against Aura, MCP check)
Dockerfile         container image for deployment (Render, etc.)
render.yaml        optional Render Blueprint (infra-as-code deploy)
```

## Notes / next steps

- **Dedup tuning**: thresholds are cosine similarity over
  `gemini-embedding-001` vectors truncated to 768 dims.
  `DUPLICATE_THRESHOLD` (default 0.97) governs the metadata-driven path;
  raise it if real new info is getting skipped within a concept.
  `EXTEND_THRESHOLD` only matters for files with no `.json` sidecar.
- **Always prefer a metadata sidecar when you can.** Without one, concept
  boundaries are guessed from embedding similarity across the whole graph,
  which struggles when your content shares a lot of domain vocabulary
  (e.g. multiple weeks of the same course) — different topics can score
  0.90+ "similar" to each other. With a sidecar, the concept is decided
  from `course`/`title`, not guessed, and dedup only checks for exact
  duplicates within that one concept.
- **Multi-user isolation**: `GraphRAGOrchestrator` keeps one Gemini chat
  history per Telegram chat ID in memory. Restarting the bot clears
  history; swap in persistent storage if you need it to survive restarts.
- **Local Neo4j instead of Aura**: a `docker-compose.yml` is still included
  if you ever want to run Neo4j locally instead — just point `NEO4J_URI` at
  `bolt://localhost:7687` and run `docker compose up -d neo4j` before step 4.
- **Production**: switch `start_polling()` to a webhook, add retries around
  the MCP subprocess, and consider running the MCP server as a long-lived
  sidecar instead of a per-orchestrator subprocess if you scale to
  multiple bot instances.
