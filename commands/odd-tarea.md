---
# NOTA: formato de comando específico de Claude Code (ver "Comandos SDD" del README.md para adaptarlo).
description: Clasifica un trabajo con ODD y, si es sustancial, crea su registro odd/tasks/NNN-slug.md
argument-hint: "<descripción del trabajo>"
---

Invoca la skill `project-scaffold` y sigue `references/odd.md`. Los scripts están en `scripts/` de la skill (en Windows usa `python` o `py`).

Trabajo solicitado: $ARGUMENTS

1. Clasifica con el test de recuperación: small o sustancial (disparadores duros → sustancial).
2. Small: impleméntalo con prueba de regresión si aplica y commit; no crees tarea.
3. Sustancial: crea el registro con `nueva_tarea.py --nombre "<nombre>" --ruta <raíz del proyecto>` y llena Specs, Tasks (con check) y Verificación.
4. Responde con la clasificación, el motivo y la ruta creada (si hubo).
