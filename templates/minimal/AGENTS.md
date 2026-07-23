# AgentSeed Agents

This file is the single source of truth for all agent roles and Party Mode behaviour.

## Skills Location (Important)

**Canonical skills directory:** `.agents/skills/`

All AgentSeed skills live under `.agents/skills/`.
Agents and tools **must** load skills from this path.

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

## Spec-Driven Workflow

1. Explore → 2. Propose → 3. Apply → 4. Verify → 5. Archive

Work under `agentseed/specs/` and `agentseed/changes/`.
