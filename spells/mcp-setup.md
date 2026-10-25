# mcp-setup — connect the external services I choose

## Cast when

- I want to connect a service: "подключи почту / календарь / GitHub / LinkedIn / Blender / браузер".
- A task needs a server that isn't connected → say so, offer this spell; cast after "yes".
- Disconnecting a service or changing its account → the same steps in reverse.

## Input

| Field | Required | Notes |
|---|---|---|
| services | yes | from the catalog `arsenal/mcp-servers/AGENTS.md`; unknown → show the catalog and ask |
| runtime | yes | which runtime(s) I use — detect what's installed (`claude`, `codex`), ask only if both |
| accounts | per server | e.g. Google aliases + e-mails, GitHub account names |

## Steps

1. Read `arsenal/mcp-servers/AGENTS.md` and `librarium/services.md` (missing →
   nothing connected yet). Show the catalog: one line per server, what it
   needs, ✓ for connected ones. Ask which to connect.
2. For each chosen server open its file `arsenal/mcp-servers/<name>.md`:
   - **Needs** → check (`node --version`, `uv --version`…). Missing → say what
     to install and skip this server until it's there.
   - Ask for the accounts / aliases it needs.
3. Write the runtime config from the file's **Config** template:
   - Claude Code → `.mcp.json` in the repo root (gitignored): merge into
     `mcpServers`, never drop or rewrite other entries; create the file if missing.
   - Codex → `~/.codex/config.toml` — outside the repo: show the block and
     ask before writing.
   - Secrets: tell me exactly where each one goes; if I paste one, write it
     there and never repeat it back. Placeholders I haven't filled → list them.
4. **Authorise** steps: commands that open a browser or ask for input → ask me
   to run them myself; others run directly.
5. Tell me to restart the runtime session — MCP servers load at start.
6. Record in `librarium/services.md`: server, accounts / aliases and what each
   is for, date connected, notes; add its row to `librarium/registry.md` if new.
   Format:

   ```
   # services — connected on this machine

   | Server | Accounts / what for | Since | Notes |
   |---|---|---|---|
   ```
7. After restart: check the server answers (one harmless read); report.

## Tools

Local file system; `node`, `uv`, `npm` (read-only checks); the server's own
auth CLI when its file says so.

## Limits

- Every service is optional: I may skip any step or server; nothing else depends on it.
- Secrets only in the MCP config / `.env` — never in `librarium/`, a tracked
  file or a reply.
- Never weaken a server's **Rules** (write deny-by-default, read-only usage,
  allowlists) without my explicit request.
- Writing outside the repo (Codex config, global npm installs) — only after "yes".

## Output

Runtime config updated, `librarium/services.md` + registry row, a short report:
connected, skipped (and why), what I still have to do.
