# Skills & MCP Inventory

This document is the checklist for what AgentSeed ships and what is still recommended.

## Skills (Canonical path: `.agents/skills/`)

### Workflow skills

| Skill | Purpose | Status |
|-------|---------|--------|
| `agentseed-explore` | Clarify intent before proposing a change | Present |
| `agentseed-propose` | Create change under `agentseed/changes/` | Present |
| `agentseed-apply` | Implement approved tasks | Present |
| `agentseed-verify` | Check implementation against specs | Present |
| `agentseed-archive` | Merge deltas into living specs | Present |
| `agentseed-party` | Multi-agent collaboration (Party Mode) | Present (strong) |

### Role skills

| Skill | Role |
|-------|------|
| `role-analyst` | Analyst |
| `role-product-manager` | Product Manager |
| `role-architect` | Architect |
| `role-developer` | Developer |
| `role-qa` | QA Engineer |
| `role-ux` | UX Designer |
| `role-tech-writer` | Technical Writer |

### Gaps / future skills (not required for v0.1)

- `agentseed-sync-skills` — copy/symlink skills into tool-specific paths
- Domain skills (e.g. `gitops-flux`, `k8s-debug`, `incident-triage`) for SRE-heavy projects
- Stronger role skills with checklists and output templates

---

## MCP (Model Context Protocol)

MCP gives agents **executable tools**. Skills give them **procedural knowledge**. Both are useful.

### Canonical config path

```text
.agents/mcp.json
```

Same neutrality principle as `.agents/skills/`.

Tool-specific mirrors (optional, via `agentseed add-mcp ... --sync`):

| Tool | Path |
|------|------|
| Cursor | `.cursor/mcp.json` |
| Claude Code | `.claude/mcp.json` |
| Codex | `.codex/config.toml` (different format; not auto-synced yet) |

### Recommended baseline MCP servers

| Server | Why |
|--------|-----|
| **filesystem** | Read/write project files, inspect structure |
| **git / github** | Branches, PRs, issues, code search |
| **memory / sequential-thinking** (optional) | Better multi-step reasoning |
| **postgres / database** (optional) | When the project has a DB |
| **kubernetes** (optional) | For platform / SRE style repos |
| **browser / playwright** (optional) | UI verification |

### CLI

```bash
agentseed list-mcp
agentseed add-mcp filesystem github
agentseed add-mcp filesystem github --sync
```

### Principles

1. MCP is optional — core skills and Party Mode work without it.
2. Prefer least-privilege servers.
3. Keep a **canonical** config under `.agents/`; mirror only when a tool cannot read that path.
4. Templates may recommend a starter set; they should not hard-require external services.
