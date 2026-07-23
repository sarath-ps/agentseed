# Recommended MCP Servers for AgentSeed

## Baseline (most projects)

### filesystem
- Read and write files in the project
- Inspect directory structure
- Essential for apply / verify workflows

### github (or git)
- Branches, pull requests, issues
- Code search across the repo
- Useful for Architect / Developer / QA roles

## Optional (by project type)

### postgres / database
- Query schemas and data when the system has a database
- Helpful for backend-heavy or polyglot monorepos

### kubernetes
- Inspect clusters, workloads, logs (when using a Kubernetes MCP server)
- Strong fit for platform / SRE style work

### browser / playwright
- UI checks and exploratory verification
- Useful with the UX and QA roles

### sequential-thinking / memory
- Extra structure for long Party Mode or multi-step design sessions

## Guidance

- Start with **filesystem + github** only.
- Add more servers only when a role or workflow clearly benefits.
- Keep secrets out of the repo; inject tokens via environment variables.
