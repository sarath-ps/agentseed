# Cursor adapter

## Discovery

| Resource | Path |
|----------|------|
| Instructions | `AGENTS.md` (and Cursor rules if you add them) |
| Skills | Canonical `.agents/skills/`; optional note under `.cursor/skills/` |
| MCP | Canonical `.agents/mcp.json`; mirror with `agentseed add-mcp … --sync` → `.cursor/mcp.json` |

Do not treat `.cursor/` as the only copy of skills or MCP.
