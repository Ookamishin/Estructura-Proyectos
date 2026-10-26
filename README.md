# estructura-proyectos

Crea proyectos con una estructura de directorios estandarizada y una carpeta `Documentacion`. Compatible con Claude Code, OpenCode, Gemini CLI y Codex CLI, en Windows, Linux y macOS.

| Tipo | Stacks |
|---|---|
| Frontend | Angular, Vue, React |
| Backend (API) | Java, Python, Node, .NET |
| Fullstack (un solo proyecto) | `java-web` (Spring+Thymeleaf), `dotnet-web` (MVC/Razor), `python-web` (Django), `node-web` (Next.js) |

## Requisitos
Python 3.9 o superior (solo biblioteca estándar). Windows: `python` o `py`; Linux/macOS: `python3`.

## Instalación
```
python3 install.py                                  # todas las herramientas, global (~/)
python3 install.py --tool claude opencode           # solo algunas
python3 install.py --scope project                  # en el proyecto actual
python3 install.py --uninstall
```

| Herramienta | Carpeta de destino (usuario / proyecto) |
|---|---|
| Claude Code | `~/.claude/skills` / `.claude/skills` |
| OpenCode | `~/.config/opencode/skills` / `.opencode/skills` |
| Gemini CLI | `~/.gemini/skills` / `.gemini/skills` |
| Codex CLI | `~/.codex/skills` / `.codex/skills` |

Rutas tomadas de la documentación pública de cada herramienta o de guías de terceros (no verificadas en una instalación real de Gemini y Codex); si tu versión usa otra, copia `skills/project-scaffold/` a la carpeta de skills que indique.

Alternativas:
- **Claude Code como plugin:** el repositorio es un plugin (`.claude-plugin/plugin.json`) e incluye `agents/scaffold-agent.md`.
- **Gemini CLI como extensión:** `gemini-extension.json` + `GEMINI.md` (que importa `AGENTS.md`).
- **Cualquier herramienta con `AGENTS.md`:** abre el repositorio y lee `AGENTS.md`.
- **ChatGPT web / apps sin acceso a archivos locales:** no pueden ejecutar el script; usa `skills/project-scaffold/proposals/*.md` como referencia.

## Uso
Pide: «crea un proyecto `mi-api` con backend .NET y frontend Angular en ~/proyectos». La skill pregunta lo que falte. Directo:

```
python3 skills/project-scaffold/scripts/scaffold.py --nombre mi-api --backend dotnet --frontend angular --ruta ~/proyectos
python3 skills/project-scaffold/scripts/scaffold.py --nombre mi-app --fullstack java-web
```

- Un solo tipo: la estructura queda en la raíz. Ambos: `backend/` y `frontend/`. `--fullstack`: un solo proyecto (no se combina con los anteriores).
- `--force` permite usar una carpeta no vacía.

## Documentacion
Cada proyecto incluye `Documentacion/backend` y/o `Documentacion/frontend`, con la propuesta `estructura-<stack>.md` y subcarpetas (arquitectura, api, decisiones, guías…). Toda documentación generada se guarda ahí. Detalle en `skills/project-scaffold/references/documentacion.md`.

## Personalizar
Edita juntos `structures/<stack>.dirs` y `proposals/<stack>.md`.
