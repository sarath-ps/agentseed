# PRD: AgentSeed 2.0

**Status:** Draft  
**Date:** 2026-07-24  
**Owner:** Sarath P.S.  
**Repo:** [sarath-ps/agentseed](https://github.com/sarath-ps/agentseed)

---

## 1. Summary

AgentSeed 2.0 turns the project from a **v0.1 method kit** into a **harness-agnostic project contract** for agentic software delivery.

It optimizes for:

- **Low $ per feature** (OpenRouter cost ladder; cheap models by default)
- **High velocity** (thin coding harnesses such as Pi for implement loops)
- **Quality gates** (spec-driven explore → propose → apply → verify → archive)
- **No harness lock-in** (Pi, Hermes, Cursor, Claude Code, Codex, and future agents load the same files)

AgentSeed is **not** an agent runtime. Runtimes (Pi, Hermes, etc.) execute work. AgentSeed defines **what every runtime must read and write** in the repository.

---

## 2. Problem

1. **Harness churn is constant.** New coding agents and personal agents appear frequently. Teams that hard-wire one tool (Cursor-only paths, Claude-only layouts, Hermes-only memory) pay repeated migration costs.
2. **Cost without policy is unbounded.** Autonomous agents on frontier models burn budget; cheap models without escalation hurt quality.
3. **Method is fragmented.** OpenSpec-style change control and BMAD-style roles exist as separate heavy systems. Teams want the useful parts without upstream lock-in.
4. **Learning does not travel.** Hermes-style memory/skills improve one install; project lessons often never land in git for the next harness or teammate.
5. **v0.1 gaps.** Skills are not always copied into new projects; MCP defaulted to Cursor-specific paths; no explicit model policy; no adapter model for new harnesses.

---

## 3. Goals

| ID | Goal | Success signal |
|----|------|----------------|
| G1 | Portable project contract | Same repo works in Pi and Hermes without rewriting core files |
| G2 | Low $/feature | ≥80% of implement tokens on L0–L1 models (policy); escalate only on verify failure or design |
| G3 | Velocity | `init` → first change proposal in minutes; apply loop stays thin |
| G4 | Quality | No “done” without verify against proposal/specs |
| G5 | Easy new harness | New adapter documented and scaffolded in ≤15 minutes |
| G6 | Optional learning | Project-level reflect → MEMORY + skills in git; Hermes personal memory remains optional |

### Non-goals

- Building a new agent runtime or competing with Hermes/Pi/Claude Code
- Reimplementing Hermes gateway, FTS5 session DB, or Honcho
- Requiring Hermes (or any single harness) to use AgentSeed
- Full BMAD character packs or OpenSpec upstream dependency
- Guaranteeing identical behaviour across all commercial IDEs

---

## 4. Users & use cases

### Primary users

- **Solo / lead engineers** running agents daily on OpenRouter (DeepSeek, GLM, Kimi) with occasional frontier escalation
- **Small teams** sharing one repo across mixed tools (Pi terminal, Hermes long-running, Cursor IDE)
- **Platform/SRE-minded builders** who want polyglot monorepo templates and clear operational conventions

### Core use cases

1. **Bootstrap** a new service or monorepo with specs, skills, MCP policy, and adapters.
2. **Implement a feature** with Pi (or similar) on L1 models; verify; archive.
3. **Architecture review** via Party Mode with cost caps; escalate Architect to L3 only.
4. **Add a new harness** (e.g. “Codex CLI”) via adapter template without forking skills.
5. **Reflect** after a non-trivial success or correction into project MEMORY/skills so the next harness benefits.
6. **Run Hermes** as optional persistent orchestrator on the same contract files.

---

## 5. Product principles

1. **Contract over runtime** — Canonical paths only under repo root / `.agents/` / `agentseed/`.
2. **Adapters, not forks** — Harness-specific notes live under `adapters/`; never a second source of truth for skills.
3. **Cost ladder by default** — Policy file names models by role; agents must follow escalation rules in AGENTS.md.
4. **Small changes** — Prefer narrow change-ids and short task lists.
5. **Quality is a gate, not a vibe** — Verify skill (or equivalent) before archive.
6. **Learning is opt-in and portable** — Prefer `.agents/skills` and `.agents/memory` in git over home-directory-only knowledge.
7. **Fork-and-go** — Clone/init works offline of OpenSpec/BMAD upstream; optional refresh later.

---

## 6. Scope

### 6.1 In scope (2.0)

**A. Core contract**

- `AGENTS.md` — roles, workflow, model policy pointer, harness-agnostic rules
- `.agents/skills/` — workflow, roles, Party Mode, **reflect**
- `.agents/mcp.json` — canonical MCP config
- `.agents/policy/models.openrouter.yaml` — cost ladder
- `.agents/policy/workflow.md` — explore → archive rules
- `.agents/memory/` — optional bounded MEMORY.md (project facts)
- `agentseed/specs|changes|party/` — living specs and changes

**B. Adapters**

```text
adapters/
  _template/
  pi/
  hermes/
  cursor/
  claude/
```

Each adapter: discovery instructions only (how that harness loads AGENTS.md, skills, MCP). Optional sync notes; no duplicated skill bodies.

**C. CLI**

| Command | Purpose |
|---------|---------|
| `agentseed init` | Templates + contract files |
| `agentseed list-templates` | |
| `agentseed list-mcp` / `add-mcp` | Canonical MCP; `--sync` mirrors |
| `agentseed adapter list\|add\|sync` | Scaffold/list adapters |
| `agentseed doctor` | Check contract presence |
| `agentseed version` | |

**D. Templates**

- `minimal` — contract + empty specs/changes
- `polyglot-monorepo` — packages skeleton + docker-compose + contract

Both ship skills (or clear copy step), policy, adapter stubs.

**E. Party Mode (retained, cost-aware)**

- Modes: session / hybrid / subagent
- Presets: ideation, architecture-review, technical-evaluation, design-review, risk-review
- Default model band: L1; architecture-review may pin Architect to L3

**F. Portable reflect (lightweight self-improvement)**

- Skill `agentseed-reflect`: after verify pass or correction, write durable facts to `.agents/memory` and/or patch/create project skills
- Explicit size budgets; no attempt to clone Hermes FTS5/Honcho

### 6.2 Out of scope (2.0)

- Native Hermes gateway integration
- Automatic npm name resolution vs avinshe/agentseed collision (document only)
- Full Codex TOML MCP auto-translation
- Multi-tenant SaaS control plane
- Fine-tuning pipelines

### 6.3 Future (post-2.0)

- `agentseed update methods` (refresh vendored OpenSpec/BMAD-inspired parts)
- `agentseed add-skill` from hub/URL
- Richer doctor (MCP connectivity, model policy lint)
- Optional session index (sqlite) for episodic search without Hermes

---

## 7. Requirements

### Functional

| ID | Requirement | Priority |
|----|-------------|----------|
| F1 | Canonical skills path is `.agents/skills/` | P0 |
| F2 | Canonical MCP path is `.agents/mcp.json` | P0 |
| F3 | AGENTS.md states harness-agnostic rules and model ladder | P0 |
| F4 | OpenRouter model policy file exists and is referenced | P0 |
| F5 | Adapter template + pi + hermes adapters documented | P0 |
| F6 | `init` installs contract into new projects (skills + policy) | P0 |
| F7 | Workflow skills: explore, propose, apply, verify, archive | P0 |
| F8 | Party Mode skill retained with cost controls | P0 |
| F9 | `agentseed-reflect` skill + memory budget rules | P1 |
| F10 | CLI `adapter` and `doctor` commands | P1 |
| F11 | `add-mcp --sync` mirrors to `.cursor` / `.claude` | P1 |
| F12 | Polyglot + minimal templates updated for 2.0 layout | P1 |
| F13 | Docs: comparison vs Hermes/Pi, cost ladder, adding a harness | P1 |

### Non-functional

| ID | Requirement |
|----|-------------|
| N1 | Core contract readable without installing the CLI |
| N2 | No hard runtime dependency on OpenSpec, BMAD, Hermes, or Pi |
| N3 | Skills follow Agent Skills / agentskills.io-style SKILL.md |
| N4 | Policy and memory files stay small enough for prompt inclusion |
| N5 | MIT license retained |

---

## 8. Model cost ladder (normative policy)

Encoded in `.agents/policy/models.openrouter.yaml` (examples; pins may change):

| Level | Role | Example band | When |
|-------|------|--------------|------|
| L0 | Triage / summarize | DeepSeek V4 Flash | Classify, route, compress |
| L1 | Default implement | DeepSeek V4 Pro / GLM-5.x | Most apply loops |
| L2 | Hard implement | Kimi K3-class | Long context, multi-file agentic |
| L3 | Design / review | Claude Sonnet / GPT mid-high | Architecture, security, repeated verify fail |
| L4 | Final gate | Opus / GPT max | Rare ship-critical review |

**Rules (AGENTS.md):**

1. Start at the lowest level that can complete the task.
2. Escalate only on verify failure, explicit design work, or user request.
3. Party Mode defaults to L1; architecture-review may use L3 for Architect only.
4. Reflect/review auxiliary calls prefer L0.

**Target economics:** ~80–90% of tokens at L0–L1; &lt;5% at L4 per feature.

---

## 9. Information architecture

```text
.
├── AGENTS.md
├── .agents/
│   ├── skills/
│   ├── mcp.json
│   ├── memory/
│   │   └── MEMORY.md
│   └── policy/
│       ├── models.openrouter.yaml
│       └── workflow.md
├── agentseed/
│   ├── specs/
│   ├── changes/
│   └── party/
├── adapters/
│   ├── _template/
│   ├── pi/
│   ├── hermes/
│   ├── cursor/
│   └── claude/
├── templates/
├── examples/mcp/
├── docs/
│   ├── PRD-AGENTSEED-2.0.md
│   ├── SKILLS_AND_MCP.md
│   └── HARNESS.md
└── src/agentseed/          # CLI
```

---

## 10. Harness matrix

| Harness | Loads AGENTS.md | Skills | MCP | Notes |
|---------|-----------------|--------|-----|-------|
| Pi | Yes (native) | Agent Skills | Via provider/tools | Preferred implement harness |
| Hermes | Via context/config | Skills path / hub | Native MCP | Preferred long-running / personal memory |
| Cursor | Rules + AGENTS | `.agents` + optional mirror | `--sync` → `.cursor/mcp.json` | IDE |
| Claude Code | CLAUDE/AGENTS patterns | skills paths | `.claude/mcp.json` mirror | |
| Codex | AGENTS.md | Varies | TOML — document only in 2.0 | |

Adding a harness = copy `adapters/_template`, fill discovery paths, optionally teach CLI `adapter add`.

---

## 11. UX / CLI flows

### New project

```bash
pip install -e .   # or uv
agentseed init shop --template polyglot-monorepo
cd shop
agentseed adapter add pi
agentseed adapter add hermes
agentseed add-mcp filesystem github --sync
agentseed doctor
```

### Feature loop (target)

1. Explore / propose (L0–L1) → `agentseed/changes/<id>/`
2. Apply with Pi on L1
3. Verify
4. On failure → escalate model or Party Mode architecture-review
5. Reflect (optional) → memory/skill
6. Archive

### Hermes overlay

- Same repo; Hermes MEMORY/USER stay in `~/.hermes` for personal facts
- Project procedures written to `.agents/skills` when portable

---

## 12. Metrics

| Metric | Target (2.0 adoption) |
|--------|----------------------|
| Time to first change proposal after init | &lt; 15 min |
| Contract files present after init | 100% (doctor pass) |
| Documented adapters | ≥ Pi + Hermes + template |
| Token share L0–L1 on sample feature | ≥ 80% (manual or logged) |
| Harness switch without rewriting skills | Pi ↔ Hermes demo path documented |

---

## 13. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Name collision with npm `agentseed` (avinshe) | Document; consider publish name `@sarath-ps/agentseed` or `agentseed-kit` |
| Cheap models fail silently | Verify gate + escalation rules |
| Reflect skill spam | Triggers only on verify pass / correction; size budgets |
| Adapter drift | Doctor + “adapters never hold skill bodies” rule |
| Over-scoping into runtime | Explicit non-goals; PR review checklist |

---

## 14. Rollout plan

| Phase | Deliverable |
|-------|-------------|
| **2.0-alpha** | PRD, AGENTS.md redesign, policy files, adapters skeleton, reflect skill draft |
| **2.0-beta** | CLI adapter/doctor, init copies full contract, templates updated, HARNESS.md |
| **2.0** | Docs complete, sample Pi + Hermes walkthrough, roadmap trim |

Suggested PR sequence:

1. Policy + AGENTS.md + PRD (this document)
2. Adapters (`_template`, pi, hermes)
3. Reflect skill + `.agents/memory`
4. CLI adapter/doctor + init improvements
5. Template + README overhaul

---

## 15. Open questions

1. Should project `USER.md` exist, or is user profile always harness-personal (Hermes-only)?
2. Publish package name to avoid npm collision?
3. Is `agentseed adapter sync` allowed to symlink into `~/.hermes/skills` or only document manual linking?
4. Minimum doctor checks for 2.0-beta vs 2.0?

---

## 16. Appendix — relationship to other tools

| Tool | Relationship |
|------|----------------|
| OpenSpec | Inspires change/delta workflow; no dependency |
| BMAD | Inspires roles + Party Mode; generic names; no dependency |
| Pi | Preferred thin coding harness; loads AGENTS.md natively |
| Hermes | Optional persistent agent; memory/skills loop; not required |
| avinshe/agentseed | Different product (AGENTS.md generator); name collision only |
| Spec Kit / Agent OS | Adjacent SDD ecosystem; AgentSeed stays lighter and adapter-first |

---

## 17. Decision

**Proceed with AgentSeed 2.0** as a harness-agnostic project contract with OpenRouter cost policy, Pi/Hermes adapters, portable reflect, and CLI support — without building a new agent runtime.
