# dou — my DOU account + public vacancy search

Server: own module `dou-mcp` (Python stdlib, public repo), installed into
`arsenal/dou-mcp/`. Tools, files, details → its `AGENTS.md`.

## Needs

- Python 3.
- The module: `spiritus run modules:install dou-mcp`.
- A DOU account.

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"dou": { "type": "stdio", "command": "python", "args": ["arsenal/dou-mcp/server.py"] }
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.dou]
command = "python"
args = ["<repo>/arsenal/dou-mcp/server.py"]
```

## Authorise

I put `DOU_EMAIL` + `DOU_PASSWORD` into the repo-root `.env` myself — or, if I
sign in to DOU with Google / LinkedIn / GitHub, `DOU_COOKIES`
(`sessionid=…; csrftoken=…` from DevTools of a logged-in browser). Restart the
session, then the `login` tool. Never paste them into the chat.

## Rules

- Read-only, low volume, my own account.
- Bulk vacancy collection stays with `it-job-searcher`.
- Anything that would change the account or contact someone — approval gate.
