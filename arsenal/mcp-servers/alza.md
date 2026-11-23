# alza — Alza.cz catalog with my prices (AlzaPlus+ / ISIC) + my orders, cart add / remove

Server: own module `alza-mcp` (Python 3 + `curl_cffi`, `playwright` for
login only), installed into `arsenal/alza-mcp/`. Tools, files, details →
its `AGENTS.md`.

## Needs

- Python 3; Chrome or Edge (else Playwright's Chromium).
- The module: `spiritus run modules:install alza-mcp`, then its own
  dependencies (`.venv` with `curl_cffi`, `playwright`):
  `python arsenal/alza-mcp/install.py`.
- An Alza account (only for my prices and the account tools; search works without).

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"alza": { "type": "stdio", "command": "python", "args": ["arsenal/alza-mcp/server.py"] }
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.alza]
command = "python"
args = ["<repo>/arsenal/alza-mcp/server.py"]
```

## Authorise

The `login` tool (or `python arsenal/alza-mcp/server.py login`) opens a
browser window; I log in there myself (the form has a Turnstile captcha). No
password in `.env` or the chat.

## Rules

- `login` pops a window — ask me first.
- `cart_add` / `cart_remove` — approval gate: show the `dry_run` result, wait
  for my OK, call once. No checkout / payment through this server.
- Human volume (2–4 s pause, hourly / daily caps); a "cooling down" stop
  after a challenge / 429 is final for now — don't retry.
- Never print or return cookies or tokens.
