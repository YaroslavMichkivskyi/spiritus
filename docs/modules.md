# Modules

A **module** is a daemon or a domain kept in its own git repo and cloned into
`daemons/<name>/` or `domains/<name>/`. The platform repo ignores it (via
`.git/info/exclude`), and the module manager writes its row into your registry.

## Use modules

```sh
spiritus run modules:list                                # catalog + yours
spiritus run modules:install <name>                      # a standard module
spiritus run modules:add <git-url> --kind daemon         # your own / private one
spiritus run modules:add <git-url> --kind domain --name career --ref v1.2
spiritus run modules:status                              # git state of every daemon / domain folder
spiritus run modules:update [name]                       # pull
spiritus run modules:remove <name>                       # refuses if work would be lost
```

What you installed is remembered in
`arsenal/spiritus-module-manager/modules.local.json` (gitignored);
`spiritus run modules:sync` (or `bootstrap`) restores it on a new machine.
Private repos work with your normal git credentials.

A module folder is a normal git repo: edit, commit and push inside it.

## VS Code

Open `spiritus.code-workspace` (repo root). It shows `spiritus` first and
every installed module as a folder of its own, each with its own repository
in Source Control; inside `spiritus` the module folders are hidden so nothing
shows twice. The module manager keeps the list in step on every
install / add / remove; `spiritus run modules:workspace` rewrites it by hand.

The file is yours and gitignored (it's created from
`arsenal/spiritus-module-manager/workspace.template.json`): add any other
repo with *File → Add Folder to Workspace…* and it stays there, never pushed.

## Make your own module

Repo root = the module folder:

```
AGENTS.md     charter, starting with frontmatter (below)
CLAUDE.md     one line: @AGENTS.md
.gitignore    keeps personal data out (e.g. data/)
...           whatever the charter defines: templates, scripts, sub-folders
```

Frontmatter — becomes your registry row:

```
---
kind: daemon
when: <when to summon it — one line>
works-for: <domains/... it serves>
---
```

```
---
kind: domain
about: <which area of life — one line>
when: <when to enter it — one line>
---
```

A shareable domain keeps its **rules, templates and scripts** in git and your
**data** in folders its own `.gitignore` excludes — whoever clones it gets the
process, not your data. A domain may carry its own daemons and spells inside
(`domains/<name>/daemons/…`), registered by its charter.

## Turn a local domain into a module

1. Add the frontmatter to `domains/<name>/AGENTS.md` and a `.gitignore`
   that excludes its personal data; check with `git status` inside step 3
   that no personal file would be committed.
2. Create an empty repo (e.g. on GitHub — private if it's only for you and
   people you invite).
3. Push the folder from inside it:
   `git init`, `git add .`, `git commit -m "…"`, `git remote add origin <url>`,
   `git push -u origin main`.
4. Let the manager take it over: rename the folder to `<name>.old`, run
   `spiritus run modules:add <url> --kind domain --name <name>`, copy your
   ignored data files from `<name>.old` into the fresh clone, delete `<name>.old`.

## Add a module to the standard catalog

Add an entry to `arsenal/spiritus-module-manager/catalog.json`:

```json
{ "modules": { "<name>": { "kind": "daemon", "url": "https://github.com/<you>/<repo>.git", "about": "<one line>" } } }
```
