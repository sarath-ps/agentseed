# AgentSeed Propose

Create a new change under `agentseed/changes/<change-id>/`.

## When to use

After exploration, when the user wants to formalise a change.

## Behaviour

1. Generate a short, unique change-id (kebab-case).
2. Create the change directory with:
   - `proposal.md` — what and why
   - `design.md` — technical decisions and trade-offs
   - `tasks.md` — implementation breakdown
   - `specs/` — deltas against living specs (if any)
3. Keep scope focused; prefer smaller changes when possible.
4. Do **not** implement production code yet — that belongs to Apply.

## Output

- Path to the new change directory
- Brief summary of proposal + main design decisions
- List of tasks
