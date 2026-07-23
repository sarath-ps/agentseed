"""AgentSeed CLI entrypoint."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from agentseed.mcp_servers import (
    get_server_config,
    get_server_description,
    list_server_names,
)

app = typer.Typer(
    name="agentseed",
    help="Lightweight framework for bootstrapping agentic AI development projects.",
    no_args_is_help=True,
)
console = Console()

# Templates are expected relative to the installed package or the repo root.
TEMPLATES = {
    "minimal": "templates/minimal",
    "polyglot-monorepo": "templates/polyglot-monorepo",
}

DEFAULT_MCP_PATH = Path(".cursor/mcp.json")


def _find_templates_root() -> Path:
    """Locate the templates directory (works both from source and installed package)."""
    # 1. Try relative to this file (source checkout)
    candidate = Path(__file__).resolve().parents[2] / "templates"
    if candidate.is_dir():
        return candidate

    # 2. Fallback: current working directory
    cwd_candidate = Path.cwd() / "templates"
    if cwd_candidate.is_dir():
        return cwd_candidate

    raise FileNotFoundError(
        "Could not locate AgentSeed templates. "
        "Run from the repository root or install the package properly."
    )


def _load_mcp_config(path: Path) -> dict:
    if not path.exists():
        return {"mcpServers": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        console.print(f"[red]Invalid JSON in {path}:[/red] {e}")
        raise typer.Exit(1)
    if "mcpServers" not in data or not isinstance(data["mcpServers"], dict):
        data["mcpServers"] = {}
    return data


def _save_mcp_config(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


@app.command()
def init(
    name: str = typer.Argument(..., help="Name of the new project directory"),
    template: str = typer.Option(
        "minimal",
        "--template",
        "-t",
        help="Template to use: minimal | polyglot-monorepo",
    ),
    force: bool = typer.Option(False, "--force", help="Overwrite if directory already exists"),
) -> None:
    """Create a new project from a template."""
    if template not in TEMPLATES:
        console.print(f"[red]Unknown template:[/red] {template}")
        console.print(f"Available: {', '.join(TEMPLATES)}")
        raise typer.Exit(1)

    target = Path.cwd() / name
    if target.exists() and not force:
        console.print(f"[red]Directory already exists:[/red] {target}")
        console.print("Use --force to overwrite.")
        raise typer.Exit(1)

    try:
        templates_root = _find_templates_root()
    except FileNotFoundError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)

    source = templates_root / TEMPLATES[template].split("/", 1)[-1]
    if not source.is_dir():
        console.print(f"[red]Template not found:[/red] {source}")
        raise typer.Exit(1)

    if target.exists() and force:
        shutil.rmtree(target)

    shutil.copytree(source, target)

    console.print(
        Panel.fit(
            f"[green]Project created[/green]\n\n"
            f"Location : {target}\n"
            f"Template : {template}\n\n"
            f"Next steps:\n"
            f"  1. cd {name}\n"
            f"  2. Ensure skills are available under .agents/skills/\n"
            f"  3. Optionally: agentseed add-mcp filesystem github\n"
            f"  4. Read AGENTS.md and start with /party ideation",
            title="AgentSeed",
        )
    )


@app.command("list-templates")
def list_templates() -> None:
    """List available project templates."""
    console.print("[bold]Available templates[/bold]\n")
    for key in TEMPLATES:
        console.print(f"  • {key}")


@app.command("list-mcp")
def list_mcp() -> None:
    """List MCP servers known to AgentSeed."""
    table = Table(title="Known MCP servers")
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    for name in list_server_names():
        table.add_row(name, get_server_description(name))
    console.print(table)
    console.print(
        "\nAdd with: [bold]agentseed add-mcp filesystem github[/bold]"
    )


@app.command("add-mcp")
def add_mcp(
    servers: Optional[list[str]] = typer.Argument(
        None,
        help="Server names to add (e.g. filesystem github). Omit to be prompted.",
    ),
    path: Path = typer.Option(
        DEFAULT_MCP_PATH,
        "--path",
        "-p",
        help="Target MCP config file (default: .cursor/mcp.json)",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite an existing server entry with the same name",
    ),
) -> None:
    """Add one or more MCP servers to the project MCP config."""
    known = list_server_names()

    if not servers:
        console.print("[bold]Available servers:[/bold]")
        for name in known:
            console.print(f"  • {name} — {get_server_description(name)}")
        console.print(
            "\nUsage: [bold]agentseed add-mcp filesystem github[/bold]"
        )
        raise typer.Exit(0)

    unknown = [s for s in servers if s not in known]
    if unknown:
        console.print(f"[red]Unknown server(s):[/red] {', '.join(unknown)}")
        console.print(f"Known: {', '.join(known)}")
        raise typer.Exit(1)

    config = _load_mcp_config(path)
    mcp_servers: dict = config.setdefault("mcpServers", {})

    added: list[str] = []
    skipped: list[str] = []

    for name in servers:
        if name in mcp_servers and not force:
            skipped.append(name)
            continue
        entry = get_server_config(name)
        if entry is None:
            continue
        mcp_servers[name] = entry
        added.append(name)

    _save_mcp_config(path, config)

    lines = [f"[green]MCP config updated[/green]: {path}\n"]
    if added:
        lines.append(f"Added   : {', '.join(added)}")
    if skipped:
        lines.append(
            f"Skipped : {', '.join(skipped)} (already present; use --force to overwrite)"
        )
    lines.append(
        "\nReload your agent / IDE so it picks up the new MCP servers."
    )
    if "github" in added:
        lines.append(
            "Set [bold]GITHUB_PERSONAL_ACCESS_TOKEN[/bold] in your environment for the github server."
        )
    if "postgres" in added:
        lines.append(
            "Set [bold]DATABASE_URL[/bold] in your environment for the postgres server."
        )

    console.print(Panel.fit("\n".join(lines), title="AgentSeed MCP"))


@app.command()
def version() -> None:
    """Show AgentSeed version."""
    from agentseed import __version__

    console.print(f"agentseed {__version__}")


if __name__ == "__main__":
    app()
