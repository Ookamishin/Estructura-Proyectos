#!/usr/bin/env python3
"""Instala la skill project-scaffold en Claude Code, OpenCode, Gemini CLI y/o Codex CLI.

Multiplataforma (Windows, Linux, macOS). Ejemplos:
  python3 install.py                       # todas las herramientas, ámbito usuario
  python3 install.py --tool claude opencode --scope project
  python3 install.py --uninstall
"""
import argparse
import shutil
from pathlib import Path

SKILL_NAME = "project-scaffold"
SOURCE = Path(__file__).resolve().parent / "skills" / SKILL_NAME

# (ámbito usuario relativo a ~, ámbito proyecto relativo al directorio actual)
TARGETS = {
    "claude": (".claude/skills", ".claude/skills"),
    "opencode": (".config/opencode/skills", ".opencode/skills"),
    "gemini": (".gemini/skills", ".gemini/skills"),
    "codex": (".codex/skills", ".codex/skills"),
}


def destination(tool: str, scope: str) -> Path:
    user_rel, project_rel = TARGETS[tool]
    base = Path.home() / user_rel if scope == "user" else Path.cwd() / project_rel
    return base / SKILL_NAME


def install(dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SOURCE, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tool", nargs="+", choices=[*TARGETS, "all"], default=["all"])
    p.add_argument("--scope", choices=("user", "project"), default="user",
                   help="user: ~/ (global); project: directorio actual")
    p.add_argument("--uninstall", action="store_true")
    args = p.parse_args()

    tools = list(TARGETS) if "all" in args.tool else args.tool
    for tool in tools:
        dest = destination(tool, args.scope)
        if args.uninstall:
            if dest.exists():
                shutil.rmtree(dest)
                print(f"[{tool}] eliminada: {dest}")
            continue
        install(dest)
        print(f"[{tool}] instalada en: {dest}")


if __name__ == "__main__":
    main()
