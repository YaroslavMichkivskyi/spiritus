# github — repos, issues, PRs through GitHub's remote MCP server

One server entry per GitHub account, named `github-<alias>`, each with its own token.

## Needs

- A personal access token per account (fine-grained preferred): grant only the
  repos and permissions Spiritus needs; reads first, writes only if I ask.

## Config

Claude Code — `.mcp.json`, `mcpServers`:

```json
"github-<alias>": {
  "type": "http",
  "url": "https://api.githubcopilot.com/mcp/",
  "headers": { "Authorization": "Bearer <PAT>" }
}
```

Codex — `~/.codex/config.toml` (remote HTTP servers; check the current Codex
docs for the exact keys of your version):

```toml
[mcp_servers.github-<alias>]
url = "https://api.githubcopilot.com/mcp/"
bearer_token_env_var = "GITHUB_PAT_<ALIAS>"
```

## Authorise

Create the token on github.com → Settings → Developer settings → Personal
access tokens; put it into the config yourself. Record in `librarium/services.md`:
alias, account, what the token may do.

## Rules

- Always say which account (`github-<alias>`) an action is for.
- Reads are free; push, PR, issue, comment, repo settings — approval gate.
- Never reuse work / employer tokens here.
