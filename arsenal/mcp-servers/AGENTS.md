# mcp-servers — catalog of optional external services

Every service Spiritus can be connected to, one file per server: what it
gives, what it needs, config templates per runtime, how to authorise, and the
**rules for using it**. All of them are optional — Spiritus works without any.
Connecting one → core spell `spells/mcp-setup.md`.

## Catalog

| Server | Gives | Needs |
|---|---|---|
| `google.md` | Gmail, Drive, Calendar, Sheets, Docs — several Google accounts by alias | Node.js, own Google Cloud OAuth client |
| `github.md` | repos, issues, PRs — one server entry per GitHub account | a GitHub personal access token per account |
| `linkedin.md` | job search, job details, profiles, companies (unofficial, browser session) | uv |
| `blender.md` | drive a local Blender: inspect / edit the scene, run `bpy`, viewport screenshots | uv, Blender + its addon |
| `browser.md` | browser automation in my own Chrome (runtime extension, not an MCP config entry) | Chrome + the runtime's browser extension |

Which ones are connected on this machine, with which accounts →
`librarium/services.md` (personal).

## Server file — `arsenal/mcp-servers/<name>.md`

```
# <name> — what it gives, one line
## Needs          — software, accounts, keys
## Config         — template per runtime: Claude Code (`.mcp.json`), Codex (`config.toml`)
## Authorise      — one-time steps (commands I run myself when they open a browser)
## Rules          — how Spiritus must use it: limits, approval-gate points, ToS risks
```

- Templates hold placeholders (`<TOKEN>`), never real values; secrets go only
  to the runtime's MCP config / `.env` (both gitignored).
- Pin package versions in templates (`pkg@1.2.3`); bump them deliberately.
- Added / removed a server file → update the catalog above.
