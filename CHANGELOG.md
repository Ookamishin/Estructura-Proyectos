# Changelog

## [0.5.0] - 2026-11-12
### Added
- Organic Driven Development (ODD) como alternativa a SDD: guía `references/odd.md`, plantilla `templates/odd/tarea.md` y `nueva_tarea.py` (registros `Documentacion/odd/tasks/NNN-slug.md`).
- `scaffold.py --metodologia sdd|odd|ambas|ninguna`; el usuario elige con qué trabajar.
- Comando de Claude Code `/odd-tarea`; `install.py` lo instala junto a los `/sdd-*`.

### Changed
- La numeración de `nueva_spec.py` y `nueva_tarea.py` es compartida (sin colisiones entre specs y tareas).
- `--sin-sdd` queda como alias obsoleto de `--metodologia ninguna`/`odd`.

## [0.4.0] - 2026-10-28
### Added
- Spec-Driven Development (SDD): guía de buenas prácticas `references/sdd.md` y plantillas `templates/sdd/` (constitución, spec, plan, tareas).
- `scaffold.py` crea `Documentacion/specs/` con la guía, la constitución y las plantillas; `--sin-sdd` lo omite.
- Flujo SDD en `SKILL.md`, `AGENTS.md` y `scaffold-agent`.
- `nueva_spec.py`: crea `Documentacion/specs/NNN-feature/` con numeración automática, plantillas llenas e índice actualizado.
- `validar_spec.py`: valida spec, plan y tareas por fase (`--fase spec|plan|tareas|implementar`).
- Comandos de Claude Code `/sdd-especificar`, `/sdd-aclarar`, `/sdd-planear`, `/sdd-tareas`, `/sdd-implementar`, `/sdd-validar`; `install.py --tool claude` los instala. Requieren adaptación para otras IA (nota en README).

## [0.3.0] - 2026-10-26
### Added
- Compatibilidad con OpenCode, Gemini CLI y Codex CLI: `install.py`, `AGENTS.md`, `GEMINI.md`, `gemini-extension.json`.
- `SKILL.md` independiente de herramientas de Claude.

### Changed
- `scaffold.ps1` reemplazado por `scaffold.py` (Python 3.9+, Windows/Linux/macOS). Los parámetros pasan a `--nombre`, `--backend`, `--frontend`, `--fullstack`, `--ruta`, `--force`.

## [0.2.0] - 2026-10-26
### Added
- Modo `-Fullstack` (`java-web`, `dotnet-web`, `python-web`, `node-web`): un solo proyecto con el mismo lenguaje en frontend y backend.
- Pregunta de tipo fullstack en el flujo de la skill.

## [0.1.0] - 2026-10-26
### Added
- Plugin `estructura-proyectos` con `scaffold-agent` y skill `project-scaffold`.
- Script `scaffold.ps1` para crear proyectos backend, frontend o ambos.
- Estructuras y propuestas `.md` para Angular, Vue, React, Java, Python, Node y .NET.
- Carpeta `Documentacion/backend|frontend` generada en cada proyecto.
