---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Implementa las tareas pendientes de una feature SDD, pruebas primero
argument-hint: "[carpeta o número de la feature] [tarea, p. ej. T004]"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Feature y tarea: $ARGUMENTS (sin feature, usa la más reciente; sin tarea, la siguiente pendiente).

1. Ejecuta `validar_spec.py <carpeta> --fase implementar`. Si hay errores, muéstralos y detente.
2. Si la spec está `Aprobada`, cámbiala a `En implementación`.
3. Trabaja tarea por tarea en orden (pruebas antes del código), respetando el plan y la estructura del proyecto; marca `[x]` en `tareas.md` al cumplir su «Hecho cuando».
4. Si encuentras algo que contradice la spec o el plan, detente y pregunta al usuario; si cambia el comportamiento, actualiza primero la spec (historial).
5. Al terminar todas las tareas: pruebas en verde, spec en estado `Implementada`, ADRs/API/CHANGELOG actualizados y `validar_spec.py <carpeta>` sin errores.
