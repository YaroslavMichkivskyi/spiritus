# rozetka — Rozetka catalog + my buyer account (bonuses, orders, cart add / remove)

Server: own module `rozetka-mcp` (Python 3 + `curl_cffi`, `playwright` for
login only), installed into `arsenal/rozetka-mcp/`. Tools, files, details →
its `AGENTS.md`.

## Needs

- Python 3; Chrome or Edge (else Playwright's Chromium).
- The module: `spiritus run modules:install rozetka-mcp`, then its own
  dependencies (`.venv` with `curl_cffi`, `playwright`):
  `python arsenal/rozetka-mcp/install.py`.
- A Rozetka account (only for the account tools; search works without).

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"rozetka": { "type": "stdio", "command": "python", "args": ["arsenal/rozetka-mcp/server.py"] }
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.rozetka]
command = "python"
args = ["<repo>/arsenal/rozetka-mcp/server.py"]
```

## Authorise

The `login` tool (or `python arsenal/rozetka-mcp/server.py login`) opens a
browser window; I log in there myself. No password in `.env` or the chat.

## Rules

- `login` pops a window — ask me first.
- `cart_add` / `cart_remove` — approval gate: show the `dry_run` result, wait
  for my OK, call once. No checkout / payment through this server.
- Human volume (2–4 s pause, hourly / daily caps); a "cooling down" stop
  after a challenge / 429 is final for now — don't retry.
- Never print or return cookies.
