# Adapter template

Copy this folder to `adapters/<harness-name>/` when adding support for a new agent runtime.

## Fill in

1. **How this harness loads project instructions** (e.g. `AGENTS.md`, system files).
2. **How it discovers skills** (path, config key, or manual install).
3. **How it loads MCP** (config path/format).
4. **OpenRouter / model selection** — point at `.agents/policy/models.openrouter.yaml`.
5. **Quirks only** — nothing that duplicates skill bodies or specs.

## Rules

- Do **not** copy `.agents/skills/` into this adapter.
- Canonical contract remains repo-root `AGENTS.md` and `.agents/*`.
- Optional mirrors (symlinks) must be documented as optional.
