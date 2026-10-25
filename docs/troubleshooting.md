# Troubleshooting

Start with `spiritus run doctor` — it names most problems and their fix.

**`spiritus`: command not found**
- Open a new terminal (PATH changes apply only to new ones; restart VS Code).
- Run `python bootstrap.py` again and answer "yes" to adding the folder to PATH.
- Meanwhile: `python arsenal/spiritus-cli/spiritus_cli.py <command>`.

**`python` not found / opens the Microsoft Store (Windows)**
Install Python from python.org with "Add to PATH", or use `py bootstrap.py`.
Settings → Apps → Advanced app settings → App execution aliases → turn off the
`python.exe` / `python3.exe` aliases.

**macOS / Linux: `python` not found** — use `python3`.

**doctor: "repo is not a git clone"** — Spiritus was downloaded as a zip.
Clone it with `git clone` instead (modules and updates need git).

**doctor: "no agent runtime"** — install Claude Code or Codex CLI
(`getting-started.md`), open a new terminal, run doctor again.

**An external service doesn't work**
- Restart the runtime session — MCP servers load at start.
- Check what the server needs (`arsenal/mcp-servers/<name>.md` → Needs):
  Node.js, uv, a valid token.
- Claude Code: `/mcp` shows each server's status. A server that times out at
  start is often launched through `npx -y` — install it globally instead.

**The agent ignores my settings** — it reads only files listed in the
registries. Check that the scroll / domain has a row in its `registry.md`.

**`modules:remove` refuses** — the module has uncommitted or unpushed work.
Commit and push inside the module folder, or pass `--force` to discard it.
