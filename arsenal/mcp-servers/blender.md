# blender — drive my local Blender

Server: `mcp-for-blender`. Inspect / edit the scene, run `bpy` code, take
viewport screenshots. Talks to an addon inside Blender over `localhost:9876`.

## Needs

- [uv](https://docs.astral.sh/uv/) and Blender. Blender's install path →
  `librarium/` (devices / programs scroll).
- The addon, once: `uvx mcp-for-blender@2.2.2 install-addon`, then enable
  "MCP for Blender" in Blender's preferences.

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"blender": {
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-for-blender@2.2.2"],
  "env": { "BLENDER_HOST": "localhost", "BLENDER_PORT": "9876",
           "DISABLE_TELEMETRY": "true", "UV_HTTP_TIMEOUT": "120" }
}
```

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.blender]
command = "uvx"
args = ["mcp-for-blender@2.2.2"]
env = { BLENDER_HOST = "localhost", BLENDER_PORT = "9876", DISABLE_TELEMETRY = "true", UV_HTTP_TIMEOUT = "120" }
```

## Authorise

None. Each session: Blender → N-panel → "Start MCP Server".

## Rules

- The socket has no auth: keep it on `localhost`, stop it when done.
- Arbitrary Python runs with my user's rights: never touch files outside the
  scene without asking; suggest saving before big changes.
- When I'm learning: after each action explain how to do it by hand (menu
  path, hotkey, key parameters).
