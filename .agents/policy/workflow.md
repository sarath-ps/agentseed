# AgentSeed workflow policy

## Change lifecycle

1. **Explore** — Clarify problem, constraints, success criteria. Read `agentseed/specs/` and relevant code.
2. **Propose** — Create `agentseed/changes/<change-id>/` with:
   - `proposal.md` — what and why
   - `design.md` — technical decisions
   - `tasks.md` — implementation checklist
   - `specs/` — deltas when living specs change
3. **Apply** — Implement only approved tasks. Prefer a thin coding harness (e.g. Pi) and L1 models.
4. **Verify** — Compare result to proposal, design, tasks, and specs. Fail closed: do not archive on fail.
5. **Archive** — Merge accepted deltas into `agentseed/specs/`; move change to `agentseed/changes/archive/`.
6. **Reflect** (optional) — If the work was non-trivial or corrected by the user, update `.agents/memory/MEMORY.md` and/or project skills under `.agents/skills/`.

## Size and cost

- Prefer small change-ids over large multi-week proposals.
- Follow `.agents/policy/models.openrouter.yaml` for model level.
- Party Mode only when multi-role perspective is worth the tokens.

## Harness notes

- Project truth lives in this repo.
- Personal agent memory (e.g. Hermes `USER.md` / home MEMORY) must not replace `AGENTS.md` or living specs.
