# browser — automation in my own Chrome

Not an MCP config entry: the runtime's browser extension connects my Chrome
to the agent (Claude Code: the "Claude in Chrome" extension).

## Needs

- Chrome with the runtime's extension installed and signed in to the same AI account.

## Config

Nothing in the repo. Allowed browsers → a scroll in `librarium/` listing each
browser I own: `deviceId`, computer, OS (the "devices" scroll).

## Authorise

Sign in to the extension; grant it site permissions as needed.

## Rules

The same AI account may be used on another device whose browser is also
connected — never drive a browser that isn't mine.
- Before the first browser action in a session: list connected browsers and
  select an allowed one (by `deviceId` from `librarium/`) explicitly; never
  broadcast to all of them.
- No allowed browser connected → stop and tell me; don't fall back to
  whatever is connected, even if it is the only one or looks local.
- Claude Code: `list_connected_browsers`, then `select_browser` with the
  allowed `deviceId`; never `switch_browser` (it broadcasts to every browser).
- Submitting forms, posting, buying, messaging — approval gate.
