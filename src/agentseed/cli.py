"""AgentSeed CLI entrypoint."""

from __future__ import annotations

import shutil
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

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
            f"  3. Read AGENTS.md and start with /party ideation",
            title="AgentSeed",
        )
    )


@app.command("list-templates")
def list_templates() -> None:
    """List available project templates."""
    console.print("[bold]Available templates[/bold]\n")
    for key in TEMPLATES:
        console.print(f"  • {key}")


@app.command()
def version() -> None:
    """Show AgentSeed version."""
    from agentseed import __version__

    console.print(f"agentseed {__version__}")


if __name__ == "__main__":
    app()
