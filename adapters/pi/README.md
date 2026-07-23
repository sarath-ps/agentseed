# Pi adapter

[Pi](https://pi.dev/) is a minimal terminal coding harness. Preferred for **apply** loops (velocity + lower token overhead).

## Discovery

| Resource | How Pi sees it |
|----------|----------------|
| Project instructions | Loads `AGENTS.md` from repo root (and parent dirs) |
| Skills | Agent Skills–compatible packages; prefer project `.agents/skills/` |
| Models | Configure OpenRouter (or other providers) in Pi; follow cost ladder in `.agents/policy/models.openrouter.yaml` |
| MCP | Use Pi/provider MCP support; canonical list remains `.agents/mcp.json` |

## Suggested use

1. Open the repo in Pi.
2. Confirm `AGENTS.md` appears in the startup context.
3. Use L1 models for implement; escalate per policy on verify failure.
4. Run explore → propose → apply → verify against `agentseed/changes/`.

## Not required

- Hermes
- Cursor-specific paths
