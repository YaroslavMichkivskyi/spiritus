# Concepts

Spiritus is a personal assistant made of **instructions for an AI agent**
plus a few tools. The agent runtime (Claude Code, Codex…) reads the
instruction files in this repo and acts on them.

## Platform vs. you

The repo is a **platform** shared by everyone who runs Spiritus. It holds
only generic structure and rules. Everything about *you* is gitignored, so
pulling updates never conflicts with your data, and nobody else's additions
grow your agent's context.

| Tracked (shared) | Gitignored (yours) |
|---|---|
| `AGENTS.md` / `CLAUDE.md` files, core spells and playbooks, tools | `librarium/` facts about you, your domains |
| `<realm>/AGENTS.md` — rules of a realm | `<realm>/registry.md` — *your* list for that realm |
| module catalog, MCP server catalog | which modules / services *you* installed, secrets |

## Realms

| Folder | What |
|---|---|
| `librarium/` | your personal library: profile, accounts, preferences ("scrolls") |
| `domains/` | areas of your life (job search, study…), each with its own rules and data |
| `daemons/` | sub-agents for bulky tasks; they return only a short result |
| `spells/` | concrete actions with input, steps and limits (`setup`, `create-domain`) |
| `playbooks/` | rules for doing a kind of work well (`self-update`) |

Other folders: `arsenal/` (tools), `assets/` (images, templates), `docs/`
(this), `laboratory/` (plans and drafts for Spiritus itself).

## Indexes and registries

The agent never reads everything. It always has the **indexes**
(`<realm>/AGENTS.md`) and **your registries** (`<realm>/registry.md`) in
context; a registry row says which file answers which question, and only that
file is opened. **Core** spells and playbooks are always active; anything else
is active only when it's in your registry.

## Modules

A daemon or a domain can live in its own git repo — a **module** — cloned
into `daemons/<name>/` or `domains/<name>/`. Standard modules are listed in a
catalog anyone can install; private ones you add by URL. See `modules.md`.

## Safety

- **Approval gate**: anything that leaves your machine — sending mail,
  posting, pushing, applying to a job — is shown to you first and done only
  after an explicit "yes". One yes = one action.
- Secrets live only in `.env` and the runtime's MCP config, both gitignored.
- External services are optional and each has its own usage rules
  (`arsenal/mcp-servers/`).
