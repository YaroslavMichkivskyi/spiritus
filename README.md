# Spiritus

A personal AI assistant you run on your own machine: job search, mail,
studies, any area of life you give it. Spiritus is a set of instructions and
small tools for an agent runtime (Claude Code or Codex); your personal data
stays local and out of git.

## Requirements

- [git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) 3.9+
- an agent runtime: [Claude Code](https://docs.claude.com/en/docs/claude-code) or [Codex CLI](https://github.com/openai/codex)
- [Node.js](https://nodejs.org/) 18+ — only for external services (most MCP servers)

## Quick start

```sh
git clone https://github.com/YaroslavMichkivskyi/spiritus.git && cd spiritus
python bootstrap.py        # macOS / Linux: python3 bootstrap.py
claude                     # or: codex
```

## Everyday

| | |
|---|---|
| check the machine | `spiritus run doctor` |
| all commands | `spiritus list` |
| install a module | `spiritus run modules:install <name>` |
| update | `git pull` and `spiritus run modules:update` |
