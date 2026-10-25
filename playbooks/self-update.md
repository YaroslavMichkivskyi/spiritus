# self-update — change Spiritus itself without breaking its structure

## Follow when

- Adding, renaming or removing a domain, daemon, spell, playbook, draft or
  `librarium/` scroll.
- Changing any instruction file (`AGENTS.md`, `CLAUDE.md`, registries,
  charters, spells, playbooks).
- Changing config: `.gitignore`, MCP servers, `.env`, permissions, launch scripts.
- Not for ordinary domain data (a new note, a new document in a domain) —
  there the domain charter's own rules are enough, plus the index rule below.
- If the change contradicts an existing rule, show me the conflict and ask
  before editing.

## Rules

1. **Pick the right place** for every new piece:

   | What | Where | In git? |
   |---|---|---|
   | fact about me (accounts, profile, CV, devices) | `librarium/<topic>.md` | no |
   | secret (token, key, password, OAuth client) | MCP config / `.env` only — never in a `.md` | no |
   | a life area: its charter and data | `domains/<name>/…` | no |
   | my list of scrolls / domains / daemons / spells / playbooks | `<realm>/registry.md` | no |
   | generic rules of a realm (any user) | `<realm>/AGENTS.md` | yes |
   | shared rule / charter / index | `AGENTS.md` of the narrowest folder it applies to | yes |
   | runtime-only detail (tool names, plugin, config path) | that runtime's file: `CLAUDE.md` for Claude Code | yes |
   | concrete action Spiritus performs | `spells/<name>.md` | yes |
   | general rules for a kind of work | `playbooks/<name>.md` | yes |
   | narrow task in a separate context | `daemons/<name>/AGENTS.md` | charter only |
   | half-built agent / spell / playbook, not wired in yet | `laboratory/drafts/<name>/` | yes (except `*.local.*`) |
   | daemon / domain as its own git repo | module, via `arsenal/spiritus-module-manager/` | its own repo; listed in `catalog.json` if standard |
   | Spiritus's own tool: launcher, custom MCP, library, script | `arsenal/<name>/` | yes |
   | an external service Spiritus can connect to | `arsenal/mcp-servers/<name>.md` (catalog) | yes |
   | which services are connected here, with which accounts | `librarium/services.md` | no |
   | a new requirement of the machine | a check in `arsenal/spiritus-setup/doctor.py` + `README.md` + `docs/getting-started.md` | yes |
   | documentation for people | `docs/<topic>.md`, linked from `README.md` | yes |
   | shared static resource (image, template, layout) | `assets/` | yes |
   | idea / to-do / experiment about Spiritus itself | `laboratory/` | yes (except `*.local.*`) |

2. **Write the instruction well:**
   - English only; data may be in any language.
   - Tool-agnostic in `AGENTS.md`: say "subagent", "web fetch", "browser
     automation", "MCP server `google`" — not a runtime's tool names.
   - `CLAUDE.md` holds only `@` imports and Claude-only specifics;
     never duplicate a shared rule there.
   - Short and concrete: every line is read on every session — cut prose,
     prefer tables and lists, no examples that don't change behaviour.
   - One rule lives in one place; elsewhere link to it.
   - Names follow the root naming rule; dates are absolute (`2026-10-11`).
   - Cross-platform (root `AGENTS.md`): no OS-only script, path or command
     without its counterpart for the other OSes.
3. **Keep the platform shareable:**
   - Tracked files hold only generic structure and rules — nothing that
     differs per user. A list of *my* things (scrolls, domains, the daemons /
     spells / playbooks I use) goes to that realm's gitignored `registry.md`,
     never to a tracked index.
   - A new shareable piece only extends the platform: it doesn't edit shared
     rules to fit one user, and it costs other users no context until they
     add it to their own registry.
4. **Keep context small:**
   - Every item appears in its realm's registry with a row saying *which
     questions it answers* / *when to use it*.
   - Big folders get their own index; archive folders are marked **Archive**
     (see `domains/AGENTS.md`).
   - New always-loaded index or registry → add it to the Realm table in root
     `AGENTS.md` and an `@` import in root `CLAUDE.md`.
   - New domain → follow the domain anatomy in `domains/AGENTS.md`.
5. **Update indexes and registries** for everything created / renamed /
   removed, in the same change — and the doc in `docs/` that describes the
   changed behaviour (commands, setup steps, what a user sees).
6. **Promoting a draft:** a draft moves from `laboratory/drafts/` to its real
   realm only on my request; then it gets a registry row there and leaves the
   drafts index in `laboratory/AGENTS.md`.
7. **Git hygiene** (the repo is a git repo):
   - `git status --short` and `git check-ignore -v <path>` — personal data,
     registries and secrets must show as ignored, instructions as tracked.
   - New folder with personal data → extend `.gitignore` first, then create it.
   - Search the staged diff for secrets (`github_pat_`, `ghp_`, `GOCSPX`,
     `MASTER_KEY=`, `TOKEN=`, private keys) before every commit.

## Limits

- Never weaken the approval gate or the secrets rule without my explicit request.
- Never move a secret into a tracked file, even temporarily.
- Local commit — after I've seen the change summary; push / PR / repo
  settings — approval gate (exact payload, wait for "yes").

## Done when

Indexes and registries match the files on disk, `git status` shows no
personal file as tracked, and I got a short report of what changed and where.
