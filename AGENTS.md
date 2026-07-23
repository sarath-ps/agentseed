# AgentSeed — Project Contract

This file is the **harness-agnostic** source of truth for roles, workflow, cost policy, and Party Mode.

Any agent runtime (Pi, Hermes, Cursor, Claude Code, Codex, …) should load this file and the canonical paths below. AgentSeed is a **project contract**, not a runtime.

---

## Canonical paths

| Path | Purpose |
|------|---------|
| `.agents/skills/` | Skills (Agent Skills / SKILL.md) |
| `.agents/mcp.json` | MCP servers (tool-neutral) |
| `.agents/policy/models.openrouter.yaml` | Model cost ladder |
| `.agents/policy/workflow.md` | explore → archive rules |
| `.agents/memory/MEMORY.md` | Bounded project memory (optional) |
| `agentseed/specs/` | Living specs |
| `agentseed/changes/` | Active and archived changes |
| `adapters/` | Per-harness discovery notes only |

**Do not** treat `.cursor/`, `.claude/`, or `~/.hermes/` as source of truth for project knowledge.

---

## Model cost ladder (OpenRouter)

Follow `.agents/policy/models.openrouter.yaml`.

| Level | Role | When |
|-------|------|------|
| **L0** | Triage / summarize | Classify, route, compress, reflect auxiliaries |
| **L1** | Default implement | Most apply loops |
| **L2** | Hard implement | Long context, multi-file, sticky failures |
| **L3** | Design / review | Architecture, security, repeated verify fail |
| **L4** | Final gate | Rare ship-critical review |

**Rules**

1. Start at the lowest level that can complete the task.
2. Escalate only on verify failure, explicit design work, or user request.
3. Party Mode defaults to **L1**; `architecture-review` may use **L3** for Architect only.
4. Prefer **Pi** (or another thin coding harness) for apply loops; use **Hermes** optionally for long-running / personal memory — not required.

Target: most tokens at L0–L1; L4 exceptional.

---

## Roles (generic)

| Role | Primary responsibility |
|------|------------------------|
| **Analyst** | Research, problem framing |
| **Product Manager** | Requirements, prioritization |
| **Architect** | Design, trade-offs |
| **Developer** | Implementation against tasks |
| **QA Engineer** | Verification, acceptance |
| **UX Designer** | Flows, usability |
| **Technical Writer** | Docs clarity |
| **Facilitator** | Party Mode orchestration |

---

## Spec-driven workflow

See `.agents/policy/workflow.md`.

1. **Explore** — clarify intent  
2. **Propose** — `agentseed/changes/<id>/` (proposal, design, tasks, deltas)  
3. **Apply** — implement only approved scope  
4. **Verify** — check against proposal and specs  
5. **Archive** — merge deltas into living specs  
6. **Reflect** (optional) — update `.agents/memory` and/or project skills after non-trivial success or correction  

---

## Party Mode

```
/party
/party ideation
/party architecture-review
/party technical-evaluation
/party design-review
/party risk-review
```

Flags: `--mode session|hybrid|subagent`, `--non-interactive "..."`

| Mode | Cost | Use |
|------|------|-----|
| `session` | Lowest | Ideation |
| `hybrid` | Balanced (default) | Everyday |
| `subagent` | Highest | Hard reviews |

Facilitation: stay in role; surface trade-offs; prefer decisions and next change-id; max rounds 8–12; rolling summary; cheap model for speaker selection when needed.

---

## Harness adapters

See `adapters/` for how Pi, Hermes, Cursor, and Claude discover this contract.  
Adding a harness = copy `adapters/_template` and document discovery paths only.

---

## Skills location

**Canonical:** `.agents/skills/`  
All AgentSeed skills live there. Tools may mirror into native paths; mirrors are not authoritative.
