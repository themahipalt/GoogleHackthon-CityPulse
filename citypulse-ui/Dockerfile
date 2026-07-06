FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy source code
COPY . .

ENV PORT=8080

EXPOSE 8080

CMD ["sh", "-c", "uv run uvicorn citypulse.main:app --host 0.0.0.0 --port ${PORT}"]