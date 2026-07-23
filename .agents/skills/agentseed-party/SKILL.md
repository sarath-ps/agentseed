# AgentSeed Party Mode

Orchestrate multi-agent collaborative discussions using the generic roles defined in AGENTS.md.

## When to use

Use when the user wants multiple perspectives, ideation, architecture review, technical evaluation, design review, risk review, or any multi-agent discussion.

## Invocation examples

- `/party`
- `/party ideation`
- `/party architecture-review`
- `/party technical-evaluation`
- `/party design-review`
- `/party risk-review`
- `/party --mode session|hybrid|subagent`
- `/party --non-interactive "review the current architecture"`

## Modes

| Mode | Behaviour | Cost |
|------|-----------|------|
| `session` | Single model voices all personas | Lowest |
| `hybrid` | Rule-based + occasional LLM selection (default) | Balanced |
| `subagent` | Independent reasoning per persona | Highest |

## Cost Optimisations

- Prefer hybrid / round-robin with preset bias.
- Use cheap model for speaker selection when needed.
- Maintain rolling summary of discussion.
- Max rounds 8–12 with early termination.
- User can force a specific speaker at any time.

## Facilitator Responsibilities

1. Load the relevant cast based on the preset.
2. Keep agents in character and encourage productive disagreement.
3. Surface trade-offs clearly.
4. Produce concrete outputs (decisions, open questions, recommended change).
5. At the end, offer a summary and optionally create a new change under `agentseed/changes/`.

## Presets

- **ideation**: Analyst + Product Manager + Architect
- **architecture-review**: Architect + Product Manager + Developer + QA (prefer subagent)
- **technical-evaluation**: Architect + Developer + QA
- **design-review**: UX + Architect + Product Manager
- **risk-review**: Architect + QA + Developer (adversarial)

## Output Format

- Clear speaker labels
- Structured final summary:
  - Key decisions
  - Open questions / risks
  - Recommended next action (link to change if created)
