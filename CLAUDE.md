@AGENTS.md
@librarium/AGENTS.md
@librarium/registry.md
@domains/AGENTS.md
@domains/registry.md
@daemons/AGENTS.md
@daemons/registry.md
@spells/AGENTS.md
@spells/registry.md
@playbooks/AGENTS.md
@playbooks/registry.md

# Claude Code specifics

Only what is true for Claude Code and no other runtime. Shared rules → `AGENTS.md`.

- Registries (`*/registry.md`) are personal and gitignored; an `@` import of
  a missing one is skipped — that realm simply has nothing registered yet.
- MCP servers are defined in `.mcp.json` (gitignored, holds secrets).

## Daemons, spells, playbooks

- Summon a daemon with the Agent tool, `subagent_type: general-purpose`.
- Spells and playbooks are plain markdown, not Claude Code skills
  (`.claude/skills/`) — keep them in `spells/` / `playbooks/` so other
  runtimes can use them.
