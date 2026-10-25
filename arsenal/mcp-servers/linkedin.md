# linkedin — job search, job details, profiles, companies

Server: `mcp-server-linkedin` (unofficial — drives a LinkedIn browser session).

## Needs

- [uv](https://docs.astral.sh/uv/) (`uvx` runs the server).
- A LinkedIn account; the server keeps its own browser session.

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"linkedin": {
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-server-linkedin@4.26.2"],
  "env": { "UV_HTTP_TIMEOUT": "120" }
}
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.linkedin]
command = "uvx"
args = ["mcp-server-linkedin@4.26.2"]
env = { UV_HTTP_TIMEOUT = "120" }
```

## Authorise

First start opens a login in the server's browser — I log in myself.

## Rules

- LinkedIn's ToS forbid automated access and may restrict the account: keep
  usage **read-only and low-volume** — a search is a few pages, not a crawl.
  Reads run without asking, so pace them yourself.
- Messages, connection requests, applications — approval gate.
