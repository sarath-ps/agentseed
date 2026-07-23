# MCP Examples

Example Model Context Protocol configurations for AgentSeed projects.

## Canonical path

AgentSeed treats this as the **source of truth**:

```text
.agents/mcp.json
```

This mirrors the skills convention (`.agents/skills/`) and stays tool-neutral.

Individual tools still look in their own places:

| Tool | Project MCP config |
|------|--------------------|
| Cursor | `.cursor/mcp.json` |
| Claude Code | `.claude/mcp.json` |
| Codex | `.codex/config.toml` (different format) |

## CLI

```bash
# Write only the canonical file
agentseed add-mcp filesystem github

# Also mirror into Cursor + Claude paths
agentseed add-mcp filesystem github --sync
```

## Files in this folder

| File | Intent |
|------|--------|
| `mcp.example.json` | Neutral example (same JSON shape as Cursor/Claude) |
| `recommended-servers.md` | Short descriptions of useful servers |

## Manual usage

1. Prefer committing `.agents/mcp.json`.
2. Use `agentseed add-mcp ... --sync` or copy/symlink into tool-specific paths as needed.
3. Reload the agent so it picks up servers.
