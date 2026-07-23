# AgentSeed

**Lightweight framework for bootstrapping agentic AI development projects.**

AgentSeed aggregates the best ideas from OpenSpec (spec-driven development) and BMAD Method (role-based agile agents) into a self-contained, fork-and-go toolkit — without hard dependencies on either project.

It gives you:

- A clear **spec-driven workflow** (`explore → propose → apply → verify → archive`)
- **Generic specialist roles** (Analyst, Product Manager, Architect, Developer, QA, UX, Technical Writer)
- **Party Mode** — multi-agent collaboration you can invoke at any time for ideation, architecture reviews, technical evaluation, design reviews, and risk reviews
- Cost-aware speaker selection and modes (`session` / `hybrid` / `subagent`)
- Project templates (`minimal`, `polyglot-monorepo`)
- A lightweight CLI (`agentseed init`, `add-mcp`, …)
- Skills that work across Cursor, Codex, Claude Code, Copilot, Antigravity/Gemini, and other tools that support the Agent Skills format

---

## Quick Start

### Option A — Use the CLI (recommended)

```bash
# From the AgentSeed repository root (or after installing the package)
pip install -e .          # or: uv pip install -e .

# Create a new project
agentseed init my-project --template minimal
agentseed init my-services --template polyglot-monorepo

# Optionally attach MCP servers
cd my-project
agentseed add-mcp filesystem github

# Other commands
agentseed list-templates
agentseed list-mcp
agentseed version
```

Then:

```bash
# Ensure skills are available under .agents/skills/
# Read AGENTS.md and start working
```

### Option B — Manual copy

1. Copy a template from `templates/` (or clone this repository).
2. Skills live under **`.agents/skills/`** (the canonical location).
3. Read `AGENTS.md` — it is the single source of truth for roles and Party Mode behaviour.
4. Start working with the workflow skills or invoke Party Mode:

```text
/party ideation
/party architecture-review
/party technical-evaluation
```

---

## CLI Usage

| Command | Description |
|---------|-------------|
| `agentseed init <name>` | Create a new project (default template: `minimal`) |
| `agentseed init <name> -t polyglot-monorepo` | Create a polyglot monorepo skeleton |
| `agentseed init <name> --force` | Overwrite the target directory if it already exists |
| `agentseed list-templates` | Show available templates |
| `agentseed list-mcp` | Show known MCP servers |
| `agentseed add-mcp <server> [server…]` | Add MCP servers to `.cursor/mcp.json` |
| `agentseed add-mcp filesystem github --force` | Overwrite existing server entries |
| `agentseed add-mcp github -p path/to/mcp.json` | Write to a custom config path |
| `agentseed version` | Print the current version |

### Examples

```bash
# Minimal project
agentseed init demo-app

# Polyglot monorepo
agentseed init platform --template polyglot-monorepo

# Attach baseline MCP servers
cd platform
agentseed add-mcp filesystem github

# See what servers AgentSeed knows about
agentseed list-mcp

# Overwrite an existing entry
agentseed add-mcp github --force
```

After `add-mcp`, reload your agent/IDE so it picks up the new servers.  
For `github`, set `GITHUB_PERSONAL_ACCESS_TOKEN` in your environment.  
For `postgres`, set `DATABASE_URL`.

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

### 5. MCP (optional)

MCP gives agents executable tools. Skills give procedural knowledge.

- Catalog and examples: `examples/mcp/` and `docs/SKILLS_AND_MCP.md`
- Install helpers: `agentseed list-mcp` / `agentseed add-mcp`

Baseline recommendation: `filesystem` + `github`.

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
├── templates/
│   ├── minimal/
│   └── polyglot-monorepo/
├── examples/mcp/             # MCP config examples
├── docs/                     # Skills & MCP inventory
├── src/agentseed/            # CLI package
├── .cursor/skills/           # Compatibility note only
├── pyproject.toml
└── README.md
```

---

## Roadmap (near-term)

- [x] Project templates (`minimal`, `polyglot-monorepo`)
- [x] `.gitignore` and MIT License
- [x] Lightweight CLI (`init`, `list-templates`, `version`)
- [x] MCP guidance + `add-mcp` / `list-mcp`
- [ ] Ability to refresh selected parts from upstream OpenSpec / BMAD when desired ("fork and go + optional reinstall")
- [ ] `agentseed add-skill` helper
- [ ] Templates auto-including skills on `init`

---

## Design Principles

- **Self-contained** — no hard runtime dependency on OpenSpec or BMAD
- **Fork-and-go** — clone and start working immediately
- **Tool-agnostic skills** — prefer the emerging neutral `.agents/skills/` location
- **Cost-aware multi-agent** — hybrid speaker selection + mode controls
- **Spec-first** — agree on intent before writing large amounts of code
- **MCP optional** — core workflows work without it; tools are additive

---

## License

MIT

---

## Contributing

This project is early. PRs that improve the core skills, Party Mode behaviour, templates, CLI, or documentation are welcome.
