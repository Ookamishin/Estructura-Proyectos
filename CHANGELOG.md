# Changelog

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
