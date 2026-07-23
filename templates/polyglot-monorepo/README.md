# Polyglot Monorepo Template

A starting layout for multi-service / polyglot projects that already includes the AgentSeed structure.

## Suggested Layout

```text
.
├── AGENTS.md
├── .agents/skills/          # copy or symlink from AgentSeed
├── agentseed/
│   ├── specs/
│   ├── changes/
│   └── party/
├── packages/
│   ├── frontend/            # e.g. Next.js / React
│   ├── backend/             # e.g. FastAPI / Nest / Go
│   ├── worker/              # background jobs / workers
│   ├── shared/              # shared types / contracts
│   └── infra/               # Terraform / Helm / Flux / Kustomize
├── apps/                   # optional app entrypoints
├── docker-compose.yml
└── README.md
```

## Getting Started

1. Copy this template as the base of a new project.
2. Ensure AgentSeed skills are available under `.agents/skills/`.
3. Start with Party Mode (`/party architecture-review` or `/party ideation`) to shape the system.
4. Use the explore → propose → apply workflow for concrete changes.

This is intentionally a **skeleton** — language choices, package managers (pnpm / Turborepo / Nx / etc.), and concrete service implementations are left to the team.
