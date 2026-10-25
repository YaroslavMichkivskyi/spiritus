# spiritus-module-manager — daemons and domains as their own git repos

A **module** is a daemon or a domain that lives in its own git repo and is
cloned into `daemons/<name>/` or `domains/<name>/`. The platform repo never
tracks it; the manager hides it via `.git/info/exclude` and writes its row
into the realm's `registry.md`.

| File | In git | What |
|---|---|---|
| `modules.py` | yes | the manager (Python 3, stdlib + `git`) |
| `catalog.json` | yes | **standard** modules anyone can install: `{"modules": {"<name>": {"kind": "daemon"\|"domain", "url": "…", "about": "…"}}}` |
| `modules.local.json` | no (`*.local.*`) | what **I** installed — catalog ones and my private ones (`url`, `kind`, optional `ref`); `sync` restores them on a new machine |
| `workspace.template.json` | yes | base of `spiritus.code-workspace` (repo root, gitignored): the platform folder + generic settings |

## Commands

Run from any folder: `spiritus run modules:<command> [args]` (root
`tasks.json`), or `python arsenal/spiritus-module-manager/modules.py <command>`.

| Command | Does |
|---|---|
| `list` | catalog + my modules, installed or not |
| `install <name> [--ref R]` | clone a standard module from `catalog.json` |
| `add <url> --kind daemon\|domain [--name N] [--ref R]` | clone my own (private) module |
| `sync` | clone every module from `modules.local.json` that is missing |
| `update [name]` | `git pull --ff-only` (or checkout the pinned `ref`), refresh registry rows |
| `status [--fetch]` | every daemon / domain folder: module / unmanaged repo / in platform repo / local folder, with branch, changes, to push / pull |
| `remove <name> [--force]` | delete the folder, its exclude line, registry row and config entry; refuses while there are uncommitted or unpushed changes |
| `workspace` | rewrite the module folders of `spiritus.code-workspace` (created from the template if missing) |

`install` / `add` / `sync` / `remove` keep `spiritus.code-workspace` in step:
`spiritus` (the repo root) first, then one folder per installed module,
hidden inside the root folder via `files.exclude`. Everything else in the
file — my own folders, settings, tasks — is left alone; comments in it are
not kept when the manager rewrites it.

Cloning / fetching is a read. The manager never commits, pushes or creates
repos — that's mine to do (or Spiritus's, through the approval gate).

## Module contract

The repo root is the module folder: `AGENTS.md` charter (+ `CLAUDE.md` with
`@AGENTS.md`) and whatever the charter defines. The charter starts with
frontmatter the manager turns into the registry row:

```
---
kind: daemon
when: <summon when — one line>
works-for: <domains/... it serves>
---
```

```
---
kind: domain
about: <what life area — one line>
when: <enter when — one line>
---
```

- A shareable module carries rules, templates and scripts; personal data
  stays in folders its own `.gitignore` excludes (e.g. `data/`).
- Edit and commit inside the module folder — it's a normal repo.
