# Getting started

## Requirements

Install these yourself first — setup checks them but never installs software.

| What | Version | Why | Get it |
|---|---|---|---|
| git | any recent | Spiritus is a git repo; modules are git repos | [git-scm.com](https://git-scm.com/downloads) |
| Python | 3.9+ | setup, the `spiritus` command, tools | [python.org](https://www.python.org/downloads/) — on Windows tick "Add to PATH" |
| An agent runtime | latest | Spiritus *is* instructions for an AI agent | [Claude Code](https://docs.claude.com/en/docs/claude-code) or [Codex CLI](https://github.com/openai/codex) |
| Node.js | 18+ | only for Node-based external services (most MCP servers) | [nodejs.org](https://nodejs.org/) |

Optional: VS Code (`spiritus.code-workspace`), a GitHub account (private modules).

## Install

```sh
git clone https://github.com/YaroslavMichkivskyi/spiritus.git
cd spiritus
python bootstrap.py        # macOS / Linux: python3 bootstrap.py
```

Bootstrap:

1. checks the requirements and stops if a required one is missing;
2. installs the `spiritus` command into `~/.local/bin`;
3. offers to put that folder on PATH (Windows: user PATH; macOS / Linux: a
   line in your shell's rc file);
4. restores your modules if you're moving from another machine;
5. tells you what to do next.

It is safe to run again any time (`spiritus run bootstrap`). `--yes` answers
every question with yes.

## First run

Open a **new** terminal (so PATH applies) in the `spiritus` folder, start your
runtime (`claude` or `codex`) and say **"set me up"**. Spiritus asks a few
questions in one go — how to address you, reply language, where you live,
which areas of life to help with — and creates your personal files. Every
question can be skipped. Connecting mail, calendar, GitHub etc. is offered at
the end and is optional.

Check the machine any time: `spiritus run doctor`.

## Update

```sh
git pull
spiritus run modules:update
spiritus run doctor
```

Your personal files are gitignored, so `git pull` never touches them.

## Move to a new machine

Personal data (`librarium/`, your domains, registries, `.env`, MCP config,
`modules.local.json`) is not in git — copy it over yourself (or keep it in
your own backup). Then clone, copy the files in, run `python bootstrap.py`:
it reinstalls your modules from `modules.local.json`.

## Uninstall

Delete `~/.local/bin/spiritus` (`spiritus.cmd` on Windows), the PATH line
bootstrap added if you no longer need it, and the `spiritus` folder.
