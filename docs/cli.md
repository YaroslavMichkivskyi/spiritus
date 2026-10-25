# The `spiritus` command

Installed by `python bootstrap.py`. Works from any folder; tasks run in the
repo root.

| Command | Does |
|---|---|
| `spiritus` / `spiritus help` | short help |
| `spiritus list` | all tasks with descriptions |
| `spiritus run <task> [args...]` | run a task; extra args are passed on |

Built-in tasks (`spiritus list` shows the current set):

| Task | Does |
|---|---|
| `doctor` | check the machine, change nothing |
| `bootstrap` | re-run setup |
| `modules:list`, `modules:install <name>`, `modules:add <url> --kind …`, `modules:update`, `modules:status`, `modules:remove <name>`, `modules:sync`, `modules:workspace` | manage modules — see `modules.md` |

Help of the tool behind a task: `spiritus run modules --help`,
`spiritus run modules:install --help`.

## Tasks

Tasks are shortcuts with no logic of their own. Shared ones are in
`tasks.json` in the repo root; your own go to `tasks.local.json` next to it
(gitignored; a task with the same name overrides the shared one).

```json
{
  "tasks": {
    "notes:sync": {
      "desc": "sync my notes: [--dry-run]",
      "run": ["{python}", "arsenal/notes/sync.py"]
    }
  }
}
```

- `run` is a list of arguments, started without a shell — the same on every OS.
- `{python}` is replaced by the Python the `spiritus` command runs on.
- Paths are relative to the repo root.

Without the command: `python arsenal/spiritus-cli/spiritus_cli.py <command>`.
