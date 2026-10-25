# External services (optional)

Spiritus can use external services through MCP servers — mail and calendar,
GitHub, LinkedIn, Blender, your browser. **None are required.**

## Connect

Tell the agent what you want: "connect my mail", "подключи GitHub". It runs
the `mcp-setup` spell: shows the catalog, checks what each server needs,
writes the runtime config, walks you through authorisation and records what
is connected in `librarium/services.md`. Restart the runtime session
afterwards — servers load at start.

Where configs go:

| Runtime | File | In git |
|---|---|---|
| Claude Code | `.mcp.json` in the repo root | no |
| Codex | `~/.codex/config.toml` | outside the repo |

Secrets (tokens, OAuth client secrets) go only there and to `.env` — never
into tracked files or `librarium/`.

## Catalog

`arsenal/mcp-servers/` — one file per server: what it gives, what it needs,
config templates for each runtime, one-time authorisation, and the rules the
agent follows when using it (e.g. LinkedIn: read-only, low volume).

## Disconnect

Say "disconnect <service>": the entry is removed from the runtime config and
`librarium/services.md`. Revoke the token / app access on the service's side yourself.

## Add a server to the catalog

Create `arsenal/mcp-servers/<name>.md` following the template in
`arsenal/mcp-servers/AGENTS.md` (Needs / Config / Authorise / Rules), with
placeholders instead of real values and a pinned package version, and add a
row to the catalog table there.
