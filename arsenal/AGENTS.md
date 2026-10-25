# arsenal — Spiritus's own tools

Custom gear Spiritus and I use to run and extend Spiritus itself: the module
manager, launchers, custom MCP servers, libraries, helper scripts. Code, not
instructions about my life — tracked in git, shareable.

## Index

| Tool | What | Use when |
|---|---|---|
| `spiritus-cli/` | the `spiritus` command: `spiritus run <task>` runs a task from root `tasks.json` from any folder | running any tool here by hand; adding a shortcut for a new tool |
| `spiritus-setup/` | `bootstrap.py` (first-time setup: requirements, `spiritus` command, PATH, modules) and `doctor.py` (checks the machine) | setting Spiritus up on a machine, something "doesn't work" and the environment may be the cause |
| `spiritus-module-manager/` | installs / updates / removes daemons and domains kept in their own git repos; keeps registries and git excludes in sync | adding a standard or private daemon / domain from a git URL, updating them, checking their git state |
| `telegram-channel/` | launcher that starts a Spiritus session reachable from a Telegram bot | I want to talk to Spiritus from my phone |

## Running from the repo root

Root `tasks.json` holds short commands that forward to the tools here — no
logic of its own; `tasks.local.json` (gitignored) adds my own. Run them with
`spiritus list` / `spiritus run <task> [args...]` from any folder
(`spiritus run modules:install cv-maker`) — see `spiritus-cli/AGENTS.md`.
Without the CLI, run the tool's script directly.

## Rules

- One tool — one folder `arsenal/<name>/` (plain-English kebab-case) with an
  `AGENTS.md`: what it does, how to run it, what it reads / writes, limits.
  Runtime-only details → that folder's `CLAUDE.md`.
- Cross-platform (root `AGENTS.md`): Python 3 / Node, stdlib first; a native
  launcher only as a `.cmd` + `.sh` pair. Paths relative to the repo root,
  resolved inside the script — the tool must work from any cwd.
- No personal data, no secrets: per-user config is `*.local.*` (gitignored)
  next to the tool, secrets stay in `.env` / the MCP config.
- A tool never writes to external services on its own (push, publish, send):
  that goes through the approval gate.
- A tool I run by hand gets its shortcuts in root `tasks.json`
  (`<tool>:<command>`), each one a single forwarding call.
- Added / renamed / removed a tool → update the index above and its tasks.
