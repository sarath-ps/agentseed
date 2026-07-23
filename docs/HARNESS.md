# Harness guide (AgentSeed 2.0)

AgentSeed is a **project contract**. Harnesses execute work.

## Recommended pairing

| Job | Harness | Model band |
|-----|---------|------------|
| Implement / refactor | Pi (or thin coding CLI) | L1 |
| Sticky multi-file work | Pi / coding CLI | L2 |
| Architecture review | Any + Party Mode | L3 for Architect |
| Long-running personal ops | Hermes (optional) | L0–L2 + policy |

## Adding a harness

1. Copy `adapters/_template` → `adapters/<name>/`
2. Document how it loads `AGENTS.md`, skills, MCP, and models
3. Do not fork skill files into the adapter
4. Optionally add CLI `adapter add` entry later

## Cost

See `.agents/policy/models.openrouter.yaml` and `AGENTS.md`.
