# AgentSeed

**Lightweight framework for bootstrapping agentic AI development projects.**

AgentSeed aggregates the best ideas from OpenSpec (spec-driven development) and BMAD Method (role-based agile agents) into a self-contained, fork-and-go toolkit — without hard dependencies on either project.

It gives you:

- A clear **spec-driven workflow** (`explore → propose → apply → verify → archive`)
- **Generic specialist roles** (Analyst, Product Manager, Architect, Developer, QA, UX, Technical Writer)
- **Party Mode** — multi-agent collaboration you can invoke at any time for ideation, architecture reviews, technical evaluation, design reviews, and risk reviews
- Cost-aware speaker selection and modes (`session` / `hybrid` / `subagent`)
- Project templates (coming next) including polyglot monorepos
- Skills that work across Cursor, Codex, Claude Code, Copilot, Antigravity/Gemini, and other tools that support the Agent Skills format

---

## Quick Start

1. Clone or use this repository as a starting point for a new project.
2. Skills live under **`.agents/skills/`** (the canonical location).
3. Read `AGENTS.md` — it is the single source of truth for roles and Party Mode behaviour.
4. Start working with the workflow skills or invoke Party Mode:

```text
/party ideation
/party architecture-review
/party technical-evaluation
```

---

## Core Concepts

### 1. Spec-Driven Changes (`agentseed/`)

```text
agentseed/
├── specs/          # Living capability specs (Requirements + Scenarios)
├── changes/        # Active proposals (proposal.md, design.md, tasks.md + deltas)
└── party/          # Optional session summaries / memory
```

Workflow:

1. **Explore** – clarify intent
2. **Propose** – formalise a change
3. **Apply** – implement the tasks
4. **Verify** – check against specs
5. **Archive** – merge deltas into living specs

### 2. Roles

Defined in `AGENTS.md`. All role names are generic and purpose-driven (no character names).

### 3. Party Mode

Multi-agent collaboration that can be started at any moment.

| Mode | Independence | Cost | Best for |
|------|--------------|------|----------|
| `session` | Low | Lowest | Ideation, quick discussion |
| `hybrid` | Medium | Balanced | Everyday use (default) |
| `subagent` | High | Highest | Architecture / design / risk reviews |

Presets include `ideation`, `architecture-review`, `technical-evaluation`, `design-review`, and `risk-review`.

### 4. Skills Location

**Canonical path:** `.agents/skills/`

Agents and tools should load skills from this directory.  
A short compatibility note is kept under `.cursor/skills/` for Cursor users.

---

## Repository Layout

```text
.
├── AGENTS.md                 # Roles + Party Mode rules + workflow guidance
├── .agents/skills/           # Canonical skills (Party Mode, workflow, roles)
├── agentseed/
│   ├── specs/
│   ├── changes/
│   └── party/
├── .cursor/skills/           # Compatibility note only
└── README.md
```

---

## Roadmap (near-term)

- [ ] Project templates (`minimal`, `polyglot-monorepo`)
- [ ] `.gitignore`, LICENSE, and repository topics
- [ ] Optional CLI (`agentseed init`, `agentseed update methods`, …)
- [ ] MCP server configuration helpers
- [ ] Ability to refresh selected parts from upstream OpenSpec / BMAD when desired ("fork and go + optional reinstall")

---

## Design Principles

- **Self-contained** — no hard runtime dependency on OpenSpec or BMAD
- **Fork-and-go** — clone and start working immediately
- **Tool-agnostic skills** — prefer the emerging neutral `.agents/skills/` location
- **Cost-aware multi-agent** — hybrid speaker selection + mode controls
- **Spec-first** — agree on intent before writing large amounts of code

---

## License

MIT (to be added in a follow-up PR)

---

## Contributing

This project is early. PRs that improve the core skills, Party Mode behaviour, templates, or documentation are welcome.
