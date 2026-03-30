# LLM Gateway

A self-hosted LLM gateway stack combining [LiteLLM](https://github.com/BerriAI/litellm) as an API proxy, [Open WebUI](https://github.com/open-webui/open-webui) as a chat interface, and [Caddy](https://caddyserver.com/) as a reverse proxy with automatic TLS.

## Architecture

- **LiteLLM** — OpenAI-compatible API proxy with spend tracking, rate limiting, and custom guardrails
- **Open WebUI** — Web-based chat interface connected to LiteLLM
- **Caddy** — Reverse proxy with automatic HTTPS via Cloudflare DNS challenge
- **PostgreSQL** — Persistent storage for LiteLLM (keys, spend logs, model config)

## Features

- **Child safety guardrail** — A custom pre-call guardrail that blocks dangerous or inappropriate content before it reaches the LLM
- **Spend tracking** — Per-key and per-model cost tracking via LiteLLM + PostgreSQL
- **Rate limiting** — Configurable RPM/TPM limits per model

## Prerequisites

- Docker and Docker Compose
- A domain with DNS managed by Cloudflare
- API key(s) for your chosen LLM provider(s)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/mrwadams/llm-gateway.git
   cd llm-gateway
   ```

2. Copy the example environment file and fill in your values:

   ```bash
   cp .env.example .env
   ```

3. Update the `Caddyfile` with your domain.

4. Start the stack:

   ```bash
   docker compose up -d
   ```

5. Access Open WebUI at your configured domain.

## Configuration

- **Models** — Add or modify models in `litellm_config.yaml`
- **Guardrails** — Edit blocked patterns in `custom_guardrail.py`
- **TLS/Domain** — Update the domain and DNS settings in `Caddyfile`
