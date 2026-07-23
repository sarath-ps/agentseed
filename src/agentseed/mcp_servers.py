"""Catalog of known MCP servers that AgentSeed can install."""

from __future__ import annotations

from typing import Any

# Each entry is a ready-to-merge fragment for mcpServers.
MCP_CATALOG: dict[str, dict[str, Any]] = {
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
        "env": {},
        "description": "Read/write project files and inspect directory structure",
    },
    "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}",
        },
        "description": "Branches, PRs, issues, and code search via GitHub API",
    },
    "memory": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"],
        "env": {},
        "description": "Persistent memory for multi-step agent sessions",
    },
    "sequential-thinking": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
        "env": {},
        "description": "Structured multi-step reasoning helper",
    },
    "postgres": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"],
        "env": {},
        "description": "Query Postgres schemas and data (requires DATABASE_URL)",
    },
}


def list_server_names() -> list[str]:
    return sorted(MCP_CATALOG.keys())


def get_server_config(name: str) -> dict[str, Any] | None:
    entry = MCP_CATALOG.get(name)
    if not entry:
        return None
    # Return only the runtime fields (exclude description)
    return {
        k: v
        for k, v in entry.items()
        if k != "description"
    }


def get_server_description(name: str) -> str:
    entry = MCP_CATALOG.get(name)
    return entry.get("description", "") if entry else ""
