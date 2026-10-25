# create-domain — set up a new domain folder and register it

## Cast when

- I ask to create / start / open a new domain ("создай домен X", "заведи
  область для Y"), or `setup.md` hands over an area of my life.
- Spiritus itself sees work that fits no registered domain and will recur —
  then propose the domain first, cast only after my "yes".
- Not for a subfolder inside an existing domain — that's the domain charter's
  business. Not for renaming / removing a domain — follow `playbooks/self-update.md`.
- A ready-made domain exists as a module (`spiritus run modules:list`) →
  offer to install it instead (`spiritus run modules:install <name>`).

## Input

| Field | Required | Notes |
|---|---|---|
| name | yes | one short English word (`career`, `study`); I may give it in Russian or as a phrase → propose the word |
| purpose | yes | which area of my life it covers, 1–2 lines |
| enter when | yes | the tasks / questions that should route here — becomes the registry row |
| layout | no | files / folders and what each holds, entry points; unknown → a minimal layout, files are created when needed |
| processes | no | recurring kinds of work and how to do them; rules specific to the domain |
| links | no | `librarium/` scrolls, other domains, daemons it relies on |

Only the name given → ask **once**, in one message, for purpose, enter-when
and anything I want in layout / processes / links. Don't invent the purpose.

## Steps

1. Read `domains/registry.md` (missing → fresh setup, created in step 5).
   Overlaps an existing domain by name or purpose → show the overlap and
   ask: new domain, or a part of the existing one?
2. Fix the name by the rules in `domains/AGENTS.md` (Domain anatomy).
3. Create `domains/<name>/AGENTS.md` (English, short):

   ````
   # <name> — <tagline>

   <purpose, 1–2 lines>

   ## Layout

   ```
   <name>/
     <file or folder>  — what it holds
   ```

   Entry points: <file(s) to open first>.

   ## How to work

   - <process: trigger → steps → where results go>
   - Facts about me → `librarium/<scroll>` (by the librarium registry).
   ````

   Apply the layout rules from `domains/AGENTS.md` (live vs **Archive**,
   own index past ~10 files, files only when needed).
4. Create `domains/<name>/CLAUDE.md` containing one line: `@AGENTS.md`.
5. Add a row to `domains/registry.md` (format in `domains/AGENTS.md`):
   `` | `<name>/` | <about> | <enter when> | ``.
6. Create any data files I asked for in the layout (data may be in any language).
7. Check git: `git check-ignore -v domains/<name>/AGENTS.md domains/registry.md`
   → both ignored (a local domain never goes to the platform repo).

## Tools

Local file system, `git` (read-only commands), `spiritus run modules:list`.

## Limits

- The domain is a **local folder**. Turning it into a shareable module (own
  repo) is a separate step on my request — `docs/modules.md`.
- No commit / push here.
- No personal data in the charter beyond what the domain's rules need —
  facts about me stay in `librarium/`, the charter links to the scroll.
- Never overwrite an existing domain folder.

## Output

`domains/<name>/` with `AGENTS.md` + `CLAUDE.md` (+ requested files), a row
in `domains/registry.md`, and a short report to me: name, registry row, layout.
