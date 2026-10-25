# daemons — index

Daemons are subagents Spiritus summons. A daemon is just **a set of
instructions plus a dedicated place**: its own folder with an `AGENTS.md`
charter. Spiritus decides *what* and *why*, the daemon does *how* and returns
the result. A daemon never talks to me directly and never writes to external
services — only Spiritus does, through the approval gate.

- **Registry** — `daemons/registry.md`: which daemons I use and when to
  summon each. Personal, gitignored, always in context. Missing → no daemons
  yet. A daemon folder not in my registry is never summoned.

A daemon folder is either **in the platform repo** (tracked here) or a
**module** — its own git repo (standard from the catalog, or my private one)
installed by `arsenal/spiritus-module-manager/`. Both work the same way.

## Daemon anatomy

```
daemons/<name>/
  AGENTS.md   — charter: role, input, output, tools, boundaries, rules
  …           — the daemon's own space (workshop, templates, scripts), as its charter defines
```

## Summoning

Spawn a general-purpose subagent with your runtime's mechanism (see its own
file, e.g. `CLAUDE.md`) and a prompt of the form:
"You are daemon `<name>`. Read `daemons/<name>/AGENTS.md` and follow it.
Input: …". Pass everything it needs — it doesn't share Spiritus's context.
Runtime without subagents → follow the charter yourself, keeping its boundaries.

Daemon or spell? A daemon when the work is bulky (lots of reading, raw search
results) and only a short result matters — it keeps Spiritus's context small.
Otherwise a spell (`spells/`). Half-built daemons live in `laboratory/drafts/`
until I ask to wire them in.

## Adding a daemon

- New folder `daemons/<name>/` with its charter → a row in the registry,
  saying *when* to summon it, so Spiritus can pick it from the registry alone.
  Registry format:

  ```
  # daemons — my registry

  | Daemon | Summon when | Works for |
  |---|---|---|
  ```
- Names — plain English, kebab-case, saying what the daemon does (`cv-maker`, `mail-triage`…).
- Imported agents (e.g. from a friend) are rewritten into a charter: keep the
  rules, drop the other person's data, history and hardcoded paths.
- In-platform daemon: its space is local, only `AGENTS.md` goes to git (see
  `.gitignore`); shareable code is opened up there explicitly, one exception
  per daemon.
- Module daemon: install / update / remove only through the module manager
  (it keeps the registry row and git excludes in sync); its charter starts
  with the frontmatter the manager reads.
