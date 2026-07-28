FROM python:3.12-slim

WORKDIR /app

# System certs for outbound TLS (Aura's neo4j+s:// and the Gemini/Telegram
# APIs are all HTTPS/TLS-secured Bolt+HTTPS endpoints).
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY common ./common
COPY ingestion ./ingestion
COPY orchestrator ./orchestrator
COPY bot ./bot
COPY scripts ./scripts
COPY schema ./schema

# No EXPOSE -- this is a long-polling worker, not a web service. It makes
# no outbound listening port and needs none opened for it to work.
CMD ["python", "-m", "bot.main"]
