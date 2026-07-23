# Hermes adapter

[Hermes Agent](https://hermes-agent.nousresearch.com/) is an optional **persistent** runtime (memory, skill learning loop, multi-channel).

AgentSeed does **not** require Hermes. Use it when you want long-running continuity; keep **project** truth in this repo.

## Discovery

| Resource | Recommendation |
|----------|----------------|
| Project instructions | Point Hermes at repo `AGENTS.md` + `agentseed/specs` as project context |
| Project skills | Prefer `.agents/skills/` so Pi/Cursor share them; avoid only writing to `~/.hermes/skills` for portable procedures |
| Personal memory | Hermes `MEMORY.md` / `USER.md` under `~/.hermes` — do not replace project MEMORY |
| MCP | Configure Hermes MCP from `.agents/mcp.json` (or sync) |
| Models | OpenRouter via Hermes providers; follow `.agents/policy/models.openrouter.yaml` |

## Split of responsibilities

- **Repo / team:** `AGENTS.md`, `.agents/skills`, `.agents/memory`, specs, changes
- **Personal / machine:** Hermes home memory and learning loop

## Self-improvement

Hermes may auto-create skills in its home directory. For anything reusable on this project, also (or instead) write to `.agents/skills/` via reflect or manually so other harnesses benefit.
