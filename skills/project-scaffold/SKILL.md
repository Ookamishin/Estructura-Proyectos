---
name: project-scaffold
description: Crea proyectos con estructura de directorios estandarizada para Angular, Vue, React (frontend) y Java, Python, Node, .NET (backend/API), con propuesta de estructura en .md y carpeta Documentacion. Usar al iniciar, crear o estandarizar un proyecto, o al generar documentación de uno.
---

# project-scaffold

## Stacks soportados
| Tipo | Stacks | Propuesta |
|---|---|---|
| frontend | `angular`, `vue`, `react` | `proposals/<stack>.md` |
| backend | `java`, `python`, `node`, `dotnet` | `proposals/<stack>.md` |
| fullstack (un solo proyecto, mismo lenguaje en ambas capas) | `java-web` (Spring+Thymeleaf), `dotnet-web` (ASP.NET MVC/Razor), `python-web` (Django), `node-web` (Next.js) | `proposals/<stack>.md` |

La lista de directorios de cada stack está en `structures/<stack>.dirs` (una ruta por línea, `#` = comentario, `{{nombre}}` = minúsculas, `{{Nombre}}` = PascalCase).

## Flujo
1. Antes de crear nada, pregunta al usuario lo que no haya indicado (solo lo que falte; con la herramienta de preguntas con opciones si tu entorno la tiene, p. ej. `AskUserQuestion`, o en texto con opciones numeradas):
   - **Tipo de proyecto:** Backend (API), Frontend, Ambos (proyectos separados) o Fullstack (un solo proyecto con el mismo lenguaje en ambas capas).
   - **Stack fullstack** (si aplica): `java-web`, `dotnet-web`, `python-web` o `node-web`. Si el usuario dice que quiere el mismo lenguaje para frontend y backend, ofrece esta opción. Un stack backend + un frontend (ej. Node + React) sigue siendo «Ambos».
   - **Lenguaje/framework backend** (si aplica): Java, Python, Node, .NET.
   - **Framework frontend** (si aplica): Angular, Vue, React.
   - **Nombre** y **ruta destino** (si no los dio, propón el directorio actual como opción por defecto).

   Pregunta la hace la sesión principal, no un subagente (no puede preguntar). Si delegas, pásale ya las respuestas.
2. Ejecuta el script (Python 3.9+, sin dependencias; Windows, Linux y macOS). Las rutas son relativas a la carpeta de esta skill:
   ```
   python3 scripts/scaffold.py --nombre <nombre> [--backend java|python|node|dotnet] [--frontend angular|vue|react] [--ruta <destino>]
   ```
   En Windows usa `python` o `py` en lugar de `python3`.
   - Solo un tipo: la estructura queda en la raíz del proyecto.
   - Ambos: `backend/` y `frontend/` bajo la raíz.
   - `--fullstack java-web|dotnet-web|python-web|node-web`: un solo proyecto en la raíz; no se combina con `--backend`/`--frontend`. La documentación se crea en ambas carpetas y la propuesta queda en `Documentacion/estructura-<stack>.md`.
   - `--force` permite usar una carpeta destino no vacía.
3. El script crea los directorios (con `.gitkeep`), copia la propuesta del stack a `Documentacion/<tipo>/estructura-<stack>.md` y genera `Documentacion/README.md` como índice.
4. Si el usuario quiere cambiar la estructura de un stack, edita `structures/<stack>.dirs` y `proposals/<stack>.md` juntos (deben coincidir).

## Regla de documentación
Toda documentación que se genere para el proyecto (arquitectura, API, decisiones, guías, etc.) se guarda en `Documentacion/`, separada por tipo:
- `Documentacion/backend/` → ver subcarpetas en `references/documentacion.md`
- `Documentacion/frontend/`

Nunca dejes documentos sueltos en la raíz del proyecto (salvo `README.md` y `CHANGELOG.md` convencionales).
