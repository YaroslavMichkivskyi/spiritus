# setup — get to know me and make Spiritus mine

The conversational half of setup; the mechanical half is `python bootstrap.py`
(`arsenal/spiritus-setup/`).

## Cast when

- I say "set me up", "настрой меня", "let's start".
- A session starts and `librarium/registry.md` is missing → offer it in one
  line first; cast only after my "yes".
- Re-run: I want to change my language, profile, areas or services.
- Not for connecting one service only — that's `mcp-setup.md` directly.

## Input

Nothing up front; everything is asked in step 3.

## Steps

1. Run `spiritus run doctor` (no `spiritus` → `python arsenal/spiritus-setup/doctor.py`).
   FAIL lines → explain the fix in plain words; `spiritus` missing → ask me to
   run `python bootstrap.py`. Warnings don't block.
2. `librarium/registry.md` exists → re-run mode: show what's set (language,
   profile, domains, modules, services) in a short list and ask what to change;
   do only that, then go to step 7.
3. Ask **once**, in one message, in the language I wrote in:
   - how to address me; name;
   - which language Spiritus should reply in;
   - where I live / my time zone (for dates, local formats);
   - which areas of life or work I want help with (a few words each);
   - anything Spiritus must always know or never do.
   Everything is optional — skipped → don't ask again, don't guess.
4. Write what I gave to `librarium/` (format and rules: `librarium/AGENTS.md`):
   - `preferences.md` — reply language, how to address me, always / never rules;
   - `personal.md` — name, location, time zone;
   - `registry.md` — one row per scroll, saying which questions it answers.
5. Areas → for each:
   - a fitting module in `spiritus run modules:list` → offer to install it;
   - otherwise offer a local domain → cast `create-domain.md` per "yes";
   - "not now" → note it in my answer, nothing is created.
6. Offer external services in one line ("mail, calendar, GitHub… — connect
   now?") → "yes" → cast `mcp-setup.md`; otherwise say it can be done any time.
7. Report: what was created / changed and where, what was skipped, what I can
   say next ("создай домен …", "подключи почту", `spiritus run doctor`).

## Tools

Local file system; `spiritus` CLI (`doctor`, `modules:list`, `modules:install`).

## Limits

- Only local files; no external writes, no commits.
- Never invent facts about me; only what I said goes to `librarium/`.
- Re-run never overwrites a scroll wholesale — edit the lines that change;
  a full replacement follows the archive rule (root `AGENTS.md`).
- No secrets in `librarium/` — tokens and keys go to the MCP config / `.env`
  via `mcp-setup.md`.

## Output

`librarium/` scrolls + registry, domains / modules I agreed to, optionally
connected services, and a short report.
