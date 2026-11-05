# djinni — my Djinni candidate account + public job search

Server: own module `djinni-mcp` (Python stdlib, public repo), installed into
`arsenal/djinni-mcp/`. Tools, files, details → its `AGENTS.md`.

## Needs

- Python 3.
- The module: `spiritus run modules:install djinni-mcp`.
- A Djinni candidate account.

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"djinni": { "type": "stdio", "command": "python", "args": ["arsenal/djinni-mcp/server.py"] }
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.djinni]
command = "python"
args = ["<repo>/arsenal/djinni-mcp/server.py"]
```

## Authorise

I put `DJINNI_EMAIL` + `DJINNI_PASSWORD` into the repo-root `.env` myself (or
`DJINNI_COOKIES` from a logged-in browser), restart the session, then the
`login` tool. Never paste them into the chat.

## Rules

- Read-only, low volume, my own account (Djinni ToS forbid automation).
- Bulk vacancy collection stays with `it-job-searcher`; this server is for
  my account and single lookups.
- Anything that would change the account or contact someone — approval gate.
