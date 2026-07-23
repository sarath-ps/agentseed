# Claude Code adapter

## Discovery

| Resource | Path |
|----------|------|
| Instructions | `AGENTS.md` / Claude project conventions |
| Skills | Canonical `.agents/skills/` |
| MCP | Canonical `.agents/mcp.json`; optional mirror `.claude/mcp.json` via `--sync` |

Follow the OpenRouter (or Anthropic) cost ladder in spirit: default cheaper models for apply; escalate for design/review.
