---
name: project-scaffold
description: Crea proyectos con estructura de directorios estandarizada para Angular, Vue, React (frontend) y Java, Python, Node, .NET (backend/API), con propuesta de estructura en .md, carpeta Documentacion y metodología de trabajo a elegir: Spec-Driven Development (SDD), Organic Driven Development (ODD), ambas o ninguna. Usar al iniciar, crear o estandarizar un proyecto, al generar documentación de uno o al especificar/planear trabajo con SDD u ODD.
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
   - **Metodología de trabajo:** SDD (specs formales: spec → plan → tareas), ODD (ligera: registro único `odd/tasks/` solo en trabajo sustancial), Ambas o Ninguna. Si no sabe, recomienda SDD para equipos/contratos estrictos y ODD para ritmo ágil.
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
   - `--metodologia sdd|odd|ambas|ninguna` (por defecto `sdd`): crea `Documentacion/specs` (SDD) y/o `Documentacion/odd` (ODD). `--sin-sdd` es un alias obsoleto.
3. El script crea los directorios (con `.gitkeep`), copia la propuesta del stack a `Documentacion/<tipo>/estructura-<stack>.md`, crea según la metodología `Documentacion/specs/` (guía SDD, `constitucion.md`, `_plantillas/`) y/o `Documentacion/odd/` (guía ODD, `_plantillas/tarea.md`, `tasks/`) y genera `Documentacion/README.md` como índice.
4. Si el usuario quiere cambiar la estructura de un stack, edita `structures/<stack>.dirs` y `proposals/<stack>.md` juntos (deben coincidir).

## Regla de documentación
Toda documentación que se genere para el proyecto (arquitectura, API, decisiones, guías, etc.) se guarda en `Documentacion/`, separada por tipo:
- `Documentacion/backend/` → ver subcarpetas en `references/documentacion.md`
- `Documentacion/frontend/`

- `Documentacion/specs/` → specs de features (SDD), transversales a backend y frontend.
- `Documentacion/odd/tasks/` → registros de trabajo sustancial (ODD).

Nunca dejes documentos sueltos en la raíz del proyecto (salvo `README.md` y `CHANGELOG.md` convencionales).

## Spec-Driven Development (SDD)
Si el proyecto usa SDD (existe `Documentacion/specs/`): cuando el usuario pida una feature o cambio de comportamiento en un proyecto, sigue `references/sdd.md` (copiada en el proyecto como `Documentacion/specs/README.md`):
1. Si no existe `Documentacion/specs/constitucion.md`, propón completarla primero.
2. Crea la feature con el script (no a mano); toma el siguiente número libre, copia las plantillas del proyecto (o las de `templates/sdd/`) y actualiza `Documentacion/README.md`:
   ```
   python3 scripts/nueva_spec.py --nombre "<nombre de la feature>" [--ruta <raíz del proyecto>] [--autor <nombre>]
   ```
3. Escribe `spec.md` (qué y por qué, sin tecnología). Marca dudas con `[POR ACLARAR: …]` y pregúntalas al usuario; no las resuelvas por tu cuenta.
4. Con la spec aprobada por el usuario (estado `Aprobada`), escribe `plan.md` (verificando la constitución) y luego `tareas.md`.
5. Implementa tarea por tarea, pruebas primero, marcando `[x]`; al terminar, pon la spec en estado `Implementada`.

Antes de pasar de fase, valida y corrige los errores que reporte (código de salida 1 si hay errores):
```
python3 scripts/validar_spec.py <carpeta de la feature | raíz del proyecto> [--fase spec|plan|tareas|implementar]
```
Revisa: `[POR ACLARAR]` pendientes, historias sin criterio de aceptación, `RF-` sin historia, sin prueba en el plan o sin tarea, tareas sin `Req:`/`Hecho cuando:` o duplicadas, estado de la spec y marcadores `<…>` sin completar.

En Claude Code, el plugin trae los comandos `/sdd-especificar`, `/sdd-aclarar`, `/sdd-planear`, `/sdd-tareas`, `/sdd-implementar` y `/sdd-validar`, que aplican este flujo.

Cambios triviales (typos, estilo, bugs de una línea) no requieren spec.

## Organic Driven Development (ODD)
Si el proyecto usa ODD (existe `Documentacion/odd/`), sigue `references/odd.md` (copiada como `Documentacion/odd/README.md`):
1. Clasifica el trabajo con el test de recuperación: small (implementa y commit, sin registro) o sustancial (contrato/API, permisos, datos, irreversible, release, seguridad; ante la duda, sustancial).
2. Sustancial: crea el registro con `python3 scripts/nueva_tarea.py --nombre "<tarea>" [--ruta <raíz>] [--autor <nombre>]` y llena Specs, Tasks (cada una con su check) y Verificación.
3. Un commit por unidad citando `S1/T1` y el check ejecutado; anota en Log y cierra con evidencia.

Comando de Claude Code: `/odd-tarea`.

## Elegir metodología
Lee qué carpetas existen: solo `specs/` → SDD; solo `odd/` → ODD; ambas → pregunta cuál aplica al trabajo (SDD si requiere spec formal; ODD para lo demás; numeración compartida). Ninguna → pregunta si quiere activar una. Para añadirla a un proyecto existente, ejecuta `scaffold.py --force --metodologia <x>` con el mismo nombre/ruta.
