"""Central config loader. Everything reads its settings from here."""
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


@dataclass(frozen=True)
class Settings:
    # Telegram
    telegram_bot_token: str

    # Gemini / Google AI Studio
    google_api_key: str
    gemini_model: str
    gemini_embedding_model: str
    embedding_dimensions: int

    # Neo4j
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    neo4j_database: str

    # MCP
    mcp_server_command: str

    # Dedup / incremental-learning thresholds
    duplicate_threshold: float
    extend_threshold: float
    top_k_similar: int


def load_settings() -> Settings:
    return Settings(
        telegram_bot_token=_require("TELEGRAM_BOT_TOKEN"),
        google_api_key=_require("GOOGLE_API_KEY"),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        gemini_embedding_model=os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001"),
        embedding_dimensions=int(os.getenv("EMBEDDING_DIMENSIONS", "768")),
        neo4j_uri=os.getenv("NEO4J_URI", "bolt://localhost:7687"),
        neo4j_username=os.getenv("NEO4J_USERNAME", "neo4j"),
        neo4j_password=_require("NEO4J_PASSWORD"),
        neo4j_database=os.getenv("NEO4J_DATABASE", "neo4j"),
        mcp_server_command=os.getenv("MCP_SERVER_COMMAND", "neo4j-mcp-server"),
        duplicate_threshold=float(os.getenv("DUPLICATE_THRESHOLD", "0.95")),
        extend_threshold=float(os.getenv("EXTEND_THRESHOLD", "0.80")),
        top_k_similar=int(os.getenv("TOP_K_SIMILAR", "3")),
    )
