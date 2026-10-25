# telegram-channel — talk to Spiritus from Telegram

Starts a Spiritus session in the repo root that also listens to a Telegram
bot, so I can write to Spiritus from my phone. The bot answers only while
that session is running.

| File | What |
|---|---|
| `start.cmd` | launcher for Windows |
| `start.sh` | the same for macOS / Linux |

Run: `arsenal/telegram-channel/start.cmd` (Windows) /
`./arsenal/telegram-channel/start.sh` (macOS, Linux) — from any folder; extra
arguments are passed to the runtime.

Supported runtimes and their setup → this folder's runtime file (`CLAUDE.md`).
My bot's handle and account → `librarium/` (by its registry).

## Rules

- Replies to Telegram: short, plain text, no local paths or secrets.
- The approval gate applies unchanged: show the exact payload in the chat and
  wait for my "yes" there before any external write / send.
- Only my own account may talk to the bot (allowlist), never "anyone".
