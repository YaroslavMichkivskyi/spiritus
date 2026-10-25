"""spiritus: run tasks from the repo's tasks.json from any folder.

    spiritus list                  tasks and what they do
    spiritus run <task> [args...]  run a task; extra args are appended to it

Tasks come from `tasks.json` in the repo root (tracked) and, if present,
`tasks.local.json` (gitignored, my own tasks; same names override). A task
runs in the repo root without a shell; `{python}` in its command is the
interpreter running this script.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [ROOT / "tasks.json", ROOT / "tasks.local.json"]


def load_tasks():
    tasks = {}
    for path in FILES:
        if path.exists():
            with open(path, encoding="utf-8") as f:
                tasks.update(json.load(f).get("tasks", {}))
    return tasks


def cmd_list(tasks):
    if not tasks:
        print(f"no tasks - add them to {FILES[0].name}")
        return 0
    width = max(len(n) for n in tasks)
    for name in sorted(tasks):
        print(f"  {name:{width}}  {tasks[name].get('desc', '')}")
    return 0


def cmd_run(tasks, name, extra):
    task = tasks.get(name)
    if task is None:
        print(f"spiritus: no task '{name}' - see `spiritus list`", file=sys.stderr)
        return 2
    command = [sys.executable if part == "{python}" else part for part in task["run"]]
    try:
        return subprocess.run(command + extra, cwd=ROOT).returncode
    except FileNotFoundError:
        print(f"spiritus: cannot start '{command[0]}'", file=sys.stderr)
        return 127
    except KeyboardInterrupt:
        return 130


def main():
    args = sys.argv[1:]
    tasks = load_tasks()
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__.strip())
        return 0
    if args[0] == "list":
        return cmd_list(tasks)
    if args[0] == "run" and len(args) >= 2:
        return cmd_run(tasks, args[1], args[2:])
    print("usage: spiritus list | spiritus run <task> [args...]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
