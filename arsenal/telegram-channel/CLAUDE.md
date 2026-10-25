@AGENTS.md

# Claude Code specifics

- Channel: the official `telegram@claude-plugins-official` plugin (research
  preview); the launchers run
  `claude --channels plugin:telegram@claude-plugins-official`.
- Bot token lives in `~/.claude/channels/telegram/.env`, the access list in
  `access.json` next to it. Policy must be `allowlist` with only my account.
- Bot avatar: `assets/spiritus-avatar.png` (set via @BotFather).
