# spiritus-setup — get a machine ready for Spiritus

The mechanical half of setup; the conversational half (profile, domains,
services) is the core spell `spells/setup.md`.

| File | What |
|---|---|
| `bootstrap.py` | first-time setup, safe to repeat; root `bootstrap.py` just runs it |
| `doctor.py` | checks the machine, changes nothing; also used by `bootstrap.py` |

## bootstrap — `python bootstrap.py [--yes]` (`python3` on macOS / Linux)

1. Requirements: Python ≥ 3.9, git, repo is a git clone → stops if missing.
   Git identity, Node.js, agent runtime (`claude` / `codex`) → reported.
2. Writes the `spiritus` shim to `~/.local/bin` (`spiritus.cmd` on Windows):
   it runs `arsenal/spiritus-cli/spiritus_cli.py` with the Python bootstrap
   was started with. A shim pointing to another Spiritus copy is replaced
   only after a "yes".
3. `~/.local/bin` not on PATH → asks, then adds it: Windows — the user `Path`
   in the registry; macOS / Linux — an `export PATH=…` line in the shell rc
   file (`~/.zshrc`, `~/.bashrc` / `~/.bash_profile`, else `~/.profile`).
4. `arsenal/spiritus-module-manager/modules.local.json` exists → `modules sync`.
5. Prints the next step: start the agent, say "set me up".

Never installs software (git, Python, Node, runtimes) — it only says what's
missing and points to `README.md`. `--yes` answers every question; without a
terminal and without `--yes`, questions are answered "no".

## doctor — `spiritus run doctor`

One line per check — `ok` / `warn` / `FAIL` with how to fix it; exit code 1
when something required is missing. Required: Python, git, git clone, an
agent runtime, the `spiritus` command. Warnings: git identity, Node.js.

## Rules

- A new requirement → a check in `doctor.py` (+ a row in `README.md`
  Requirements and `docs/getting-started.md`).
- Nothing here installs third-party software or writes outside the repo,
  except the shim and the PATH entry — both announced, PATH only after "yes".
