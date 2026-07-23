# AgentSeed Agents

This file is the single source of truth for all agent roles and Party Mode behaviour.

## Skills Location (Important)

**Canonical skills directory:** `.agents/skills/`

All AgentSeed skills live under `.agents/skills/`.  
Agents and tools **must** load skills from this path.

This location was chosen for broader compatibility across tools (Cursor, Codex, Claude Code, Copilot, Antigravity/Gemini, etc.). Individual tools may also look in their native paths (`.cursor/skills/`, `.claude/skills/`, …). When in doubt, prefer `.agents/skills/`.

## Roles (Generic)

| Role | Primary Responsibility |
|------|------------------------|
| **Analyst** | Research, problem framing, opportunity analysis |
| **Product Manager** | Requirements, prioritization, stories / PRD |
| **Architect** | System design, technical decisions, trade-offs |
| **Developer** | Implementation against specs and tasks |
| **QA Engineer** | Verification, test strategy, acceptance criteria |
| **UX Designer** | User flows, interaction design, usability |
| **Technical Writer** | Documentation, clarity, living docs |
| **Facilitator** | Orchestrates Party Mode (optional meta-role) |

## Party Mode

Invoke at any time with:

```
/party
/party ideation
/party architecture-review
/party technical-evaluation
/party design-review
/party risk-review
```

Optional flags:
- `--mode session|hybrid|subagent`
- `--non-interactive "..."`

### Modes (Cost Profiles)

| Mode | Independence | Cost | Recommended Use |
|------|--------------|------|-----------------|
| `session` | Low | Lowest | Ideation, quick discussion |
| `hybrid` | Medium | Balanced | Everyday (default) |
| `subagent` | High | Highest | Architecture / design / risk reviews |

### Facilitation Rules

- Agents stay strictly in character.
- Disagreements and trade-offs must be surfaced explicitly.
- Prefer concrete outputs: decisions, open questions, recommended next change.
- At session end, produce a summary and optionally seed a new change under `agentseed/changes/`.

### Speaker Selection (Cost Optimised)

1. Prefer rule-based / round-robin with preset bias.
2. Use a cheap/fast model for facilitator decisions when LLM selection is required.
3. Maintain a rolling summary instead of full history.
4. Enforce max rounds (default 8–12) + early termination on consensus.
5. User can override at any time (“Architect, respond next”).

## Spec-Driven Workflow

Work through the OpenSpec-inspired structure under `agentseed/`:

1. **Explore** – clarify intent
2. **Propose** – create change with proposal.md / design.md / tasks.md + spec deltas
3. **Apply** – implement the tasks
4. **Verify** – check against specs and acceptance criteria
5. **Archive** – merge deltas into living specs

All agents should prefer reading and updating files under `agentseed/specs/` and `agentseed/changes/`.
