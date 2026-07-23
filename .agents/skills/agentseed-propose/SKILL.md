# AgentSeed Propose

Create a new change under `agentseed/changes/<change-id>/` with:

- `proposal.md`
- `design.md`
- `tasks.md`
- Spec deltas under `specs/`

## When to use

After exploration, when the user wants to formalise a change.

## Behaviour

1. Generate a short, unique change-id (kebab-case).
2. Write the proposal, design decisions, and task breakdown.
3. Create delta files for any affected living specs.
4. Do **not** implement code yet — that belongs to Apply.
