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
- `--sin-sdd` omite la carpeta `Documentacion/specs`.

## Documentacion
Cada proyecto incluye `Documentacion/backend` y/o `Documentacion/frontend`, con la propuesta `estructura-<stack>.md` y subcarpetas (arquitectura, api, decisiones, guías…). Toda documentación generada se guarda ahí. Detalle en `skills/project-scaffold/references/documentacion.md`.

## Spec-Driven Development (SDD)
Cada proyecto incluye `Documentacion/specs/` para trabajar con especificaciones como fuente de verdad:

- `README.md`: guía de buenas prácticas SDD (flujo spec → plan → tareas → implementación, puertas de calidad, antipatrones, uso con agentes de IA).
- `constitucion.md`: principios no negociables del proyecto.
- `_plantillas/`: `spec.md`, `plan.md` y `tareas.md`. Cada feature va en `specs/NNN-nombre-feature/`.

Pide al agente «especifica la feature de login» y seguirá el flujo. La guía fuente está en `skills/project-scaffold/references/sdd.md`.

Scripts (cualquier herramienta, Python 3.9+):
```
python3 skills/project-scaffold/scripts/nueva_spec.py --nombre "login de usuarios" --ruta ~/proyectos/mi-api
python3 skills/project-scaffold/scripts/validar_spec.py ~/proyectos/mi-api/Documentacion/specs/001-login-de-usuarios --fase plan
```
- `nueva_spec.py`: crea `specs/NNN-nombre/` con el siguiente número, copia las plantillas (las del proyecto si existen) y registra la feature en `Documentacion/README.md`.
- `validar_spec.py`: revisa una feature o todas las del proyecto; con `--fase spec|plan|tareas|implementar` exige lo necesario para avanzar. Sale con código 1 si hay errores.

### Comandos SDD (solo Claude Code)
`commands/` contiene `/sdd-especificar`, `/sdd-aclarar`, `/sdd-planear`, `/sdd-tareas`, `/sdd-implementar` y `/sdd-validar`. Se cargan con el plugin (como `/estructura-proyectos:sdd-…`) o con `python3 install.py --tool claude` (en `~/.claude/commands`).

> **Nota:** estos comandos usan el formato de Claude Code (Markdown con frontmatter y `$ARGUMENTS`). Para usarlos con otra IA hay que adaptarlos a su formato: Gemini CLI usa archivos `.toml` en `commands/` con `prompt` y `{{args}}`; OpenCode y Codex CLI usan `.md` en su propia carpeta de comandos/prompts. Verifica el formato en la documentación de cada herramienta. Sin comandos, cualquier IA puede seguir el mismo flujo pidiéndolo en lenguaje natural, ya que la skill y los scripts son comunes.

## Personalizar
Edita juntos `structures/<stack>.dirs` y `proposals/<stack>.md`.
