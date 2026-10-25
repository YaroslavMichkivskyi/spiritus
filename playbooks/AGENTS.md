# playbooks — index

A playbook is a **set of rules for doing one kind of work right**: where things
go, what good looks like, checks before finishing. It is general — it applies
to many concrete tasks of that kind. Spiritus follows a playbook whenever its
trigger fires, alongside whatever spell or task it is doing.

Playbook or spell? Playbook — *how to do X well* (rules, checklists, quality
bar). Spell (`spells/`) — *one concrete action* with its input, commands and
output (`search-jobs`, `send-mail`). A spell may follow a playbook; a playbook
never performs an action on its own.

- **Core playbooks** — part of the platform, always active, no registry row needed:

  | Playbook | Follow when |
  |---|---|
  | `self-update.md` | changing Spiritus itself: rules, indexes, registries, new / renamed domain, daemon, spell, playbook or scroll, config, gitignore |

- **Registry** — `playbooks/registry.md`: the other playbooks I use and when
  to follow each. Personal, gitignored, always in context. Missing → only the
  core ones.

## Playbook anatomy — `playbooks/<name>.md`

```
# <name> — one line saying what kind of work it governs
## Follow when    — triggers; also when it does NOT apply
## Rules          — numbered, concrete, checkable
## Limits         — what must never be done; approval-gate points
## Done when      — checks before reporting the work finished
```

- One playbook — one kind of work. Names: plain-English kebab-case, noun or
  verb phrase (`self-update`, `git-commits`).
- Tool-agnostic, in English; runtime-specific notes go to that runtime's file.
- Added / renamed / removed a playbook → update the registry. Registry format:

  ```
  # playbooks — my registry

  | Playbook | Follow when |
  |---|---|
  ```
- Shareable: no personal data, no secrets.
