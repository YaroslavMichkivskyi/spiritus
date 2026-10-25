# spells — index

A spell is **one concrete action** Spiritus casts itself, in its own context:
when to cast it, the input, the exact steps and commands, which tools to use,
the limits it must not cross and what it produces. A spell has no folder of
its own and no data — results go to the domain the work belongs to.

Spell, playbook or daemon?
- Spell — a concrete action Spiritus performs directly (`search-jobs`, `send-mail`).
- Playbook (`playbooks/`) — general rules for doing a kind of work right; no action of its own.
- Daemon (`daemons/`) — bulky work in a separate context that returns only a
  short result. A spell may summon a daemon as one step.

- **Registry** — `spells/registry.md`: the spells I use and when to
  cast each. Personal, gitignored, always in context. Missing → no spells
  yet. A spell not in my registry is never cast.

## Spell anatomy — `spells/<name>.md`

```
# <name> — one line saying what it does
## Cast when      — triggers; also when NOT to cast it
## Input          — what must be known before starting (ask if missing)
## Steps          — numbered, concrete commands / calls
## Tools          — services / MCP servers / scripts used, read or write
## Limits         — what the spell must never do; approval-gate points
## Output         — what is produced and where it is stored
```

- One spell — one action. Names: plain-English kebab-case, verb-first
  (`search-jobs`, `send-mail`).
- Tool-agnostic, in English (root `AGENTS.md`); runtime-specific steps go to
  that runtime's file.
- A spell that runs a script keeps the script next to it as `spells/<name>.<ext>`
  — deterministic work in scripts, judgement in the spell.
- Added / renamed / removed a spell → update the registry: the row says
  *when* to cast it, so Spiritus can pick it from the registry alone.
  Registry format:

  ```
  # spells — my registry

  | Spell | Cast when |
  |---|---|
  ```
- Spells are shareable: no personal data, no secrets — link to the
  `librarium/` scroll instead.
