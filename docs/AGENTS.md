# docs — documentation for people

Explanations and how-tos for the person running Spiritus; `README.md` in the
root links here. Rules for the agent live in the `AGENTS.md` files, not here —
a doc explains and links to them, never restates them as its own rules.

## Index

| File | What |
|---|---|
| `getting-started.md` | requirements, install, first run, update, move to a new machine, uninstall |
| `concepts.md` | how Spiritus is built: realms, indexes vs personal registries, core vs mine, modules, approval gate |
| `cli.md` | the `spiritus` command, `tasks.json` / `tasks.local.json`, adding a task |
| `modules.md` | installing standard / private modules, making and publishing your own, the frontmatter contract |
| `services.md` | optional external services (MCP), connecting / disconnecting, adding a server to the catalog |
| `troubleshooting.md` | common problems and their fixes |

## Rules

- Written in English for any reader; short sections, commands per OS where they differ.
- Behaviour changed (a command, a setup step, a rule a user sees) → update the
  doc that describes it in the same change.
- Added / renamed / removed a doc → update the index above and the links in `README.md`.
