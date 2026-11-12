---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Descompone el plan en tareas.md pequeñas y verificables
argument-hint: "[carpeta o número de la feature]"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Feature: $ARGUMENTS (si no se indica, usa la más reciente de `Documentacion/specs/`).

1. Ejecuta `validar_spec.py <carpeta> --fase tareas`. Si hay errores, muéstralos y detente.
2. Llena `tareas.md` agrupando por historia (P1 primero): preparación, pruebas antes de implementación, integración y cierre.
3. Cada tarea: `- [ ] T001 [P]? descripción en <ruta> — Req: RF-001 — Hecho cuando: <verificación>`; ≤ medio día; `[P]` solo si toca archivos distintos sin dependencias; `Req: —` si no cubre un requisito.
4. Todo `RF-` de la spec debe quedar cubierto por al menos una tarea.
5. Ejecuta `validar_spec.py <carpeta> --fase implementar` y corrige hasta que no haya errores.
