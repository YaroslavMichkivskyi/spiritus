# google — Gmail, Drive, Calendar, Sheets, Docs for several Google accounts

Server: [`mcp-google-multi`](https://www.npmjs.com/package/mcp-google-multi).
Accounts are addressed by alias (`work`, `personal`…).

## Needs

- Node.js; install the server globally: `npm i -g mcp-google-multi`
  (update: `npm update -g mcp-google-multi`). Launch it via its global
  command, not `npx -y` — npx hits the registry on every start and can blow
  the runtime's MCP start timeout.
- A Google Cloud project with an **OAuth client of type Desktop** (client id +
  secret); one client serves all accounts. Publish the consent screen
  ("In production"), otherwise refresh tokens expire after 7 days.
- A random `MASTER_KEY` — encrypts the stored tokens; keep it the same in the
  MCP config and `.env`, or stored tokens can't be decrypted.

## Config

Env vars (same values in the MCP config and in `.env`, which the auth CLI reads):

| Var | Value |
|---|---|
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | the Desktop OAuth client |
| `GOOGLE_ACCOUNTS` | `alias:email,alias:email` |
| `MASTER_KEY` | random secret, e.g. `python -c "import secrets; print(secrets.token_hex(32))"` |
| `GOOGLE_WRITE_ALLOW` | optional; writes are deny-by-default — open only what's needed |

Claude Code — `.mcp.json`, `mcpServers`:

```json
"google": {
  "type": "stdio",
  "command": "mcp-google-multi",
  "env": { "GOOGLE_CLIENT_ID": "<ID>", "GOOGLE_CLIENT_SECRET": "<SECRET>",
           "GOOGLE_ACCOUNTS": "<alias:email,...>", "MASTER_KEY": "<KEY>" }
}
```

On Windows `command` is the full path of the global shim
(`npm prefix -g` → `<prefix>\mcp-google-multi.cmd`).

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.google]
command = "mcp-google-multi"
env = { GOOGLE_CLIENT_ID = "<ID>", GOOGLE_CLIENT_SECRET = "<SECRET>", GOOGLE_ACCOUNTS = "<alias:email,...>", MASTER_KEY = "<KEY>" }
```

## Authorise

Once per account, from the repo root (reads `.env` in the cwd):
`npx mcp-google-multi auth --account <alias>` — opens a browser; I run it myself.

## Rules

- Pick the account by purpose (`librarium/services.md` → which alias is for what), not by habit.
- Reading mail / files is free; sending, creating events, editing documents — approval gate.
- Mail contents stay local: summaries and drafts go to the domain the work belongs to.
