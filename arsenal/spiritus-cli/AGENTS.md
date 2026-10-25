# spiritus-cli — the `spiritus` command

A tiny task runner: reads tasks from the repo root and runs them there, from
whatever folder I'm in. No logic of its own — tasks only forward to scripts.

| File | What |
|---|---|
| `spiritus_cli.py` | the runner (Python 3, stdlib only) |

## Install

`python bootstrap.py` in the repo root (see `arsenal/spiritus-setup/`) writes
a shim `spiritus` (`spiritus.cmd` on Windows) into `~/.local/bin` that runs
this script with the Python bootstrap ran on, and puts that folder on PATH.
Edits to the runner or to `tasks.json` apply at once. Without the shim:
`python arsenal/spiritus-cli/spiritus_cli.py <command>`.

## Use

| Command | Does |
|---|---|
| `spiritus`, `spiritus help` | short help |
| `spiritus list` | every task and what it does |
| `spiritus run <task> [args...]` | runs the task in the repo root; extra args are appended |

## Tasks — root `tasks.json` (+ `tasks.local.json`, gitignored)

```json
{ "tasks": { "<tool>:<command>": { "desc": "what it does: <args>", "run": ["{python}", "arsenal/<tool>/<script>.py", "<command>"] } } }
```

- `run` is an argv list, started without a shell — no quoting, same on every OS.
- `{python}` → the interpreter running `spiritus` (no `python` / `python3` guessing).
- Paths are relative to the repo root; a task in `tasks.local.json` with the
  same name overrides the shared one.
