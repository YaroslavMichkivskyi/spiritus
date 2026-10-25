# domains — index

The main storage Spiritus operates on. A domain is one area of my life with
its own data, rules and processes.

- **Registry** — `domains/registry.md`: which domains exist and when to enter
  each. Personal (every user has their own set), gitignored, always in
  context. Missing → no domains yet.
- Entering a domain → read its `AGENTS.md` first; it extends the root rules
  and wins inside the domain.
- Facts about me live in `librarium/`, not in domains; a domain links to the
  scroll it needs.
- Everything under `domains/` except this index is personal — the registry,
  every domain's charter and data stay out of git. Generic rules about
  domains belong here, never in a domain charter.

A domain folder is either a **local folder** (personal, never leaves this
machine) or a **module** — its own git repo I can share, installed by
`arsenal/spiritus-module-manager/`. A module domain keeps rules, templates
and scripts in its repo and my data in folders its own `.gitignore` excludes.

## Domain anatomy

```
domains/<name>/
  AGENTS.md   — charter: purpose, layout (files / folders, entry points), how to work
  CLAUDE.md   — one line: @AGENTS.md
  …           — the domain's data, as its charter defines
```

- Name — one lowercase English word, not taken, not a top-level folder name.
- Live data apart from archive (superseded versions, raw dumps, history,
  closed items). Archive folders are marked **Archive** in the layout and
  created only once there is something to put there.
- A subfolder grown past ~10 files → give it its own index and name it in
  the charter.
- Files are created when needed, not up front.

## Adding a domain

Spiritus may propose a domain for recurring work that fits no registered
one, but creates it only after my "yes". Then: the folder with its charter
→ a row in the registry, saying *when* to enter it (a module domain gets its
row from the module manager). Registry format:

```
# domains — my registry

| Domain | About | Enter when |
|---|---|---|
```
