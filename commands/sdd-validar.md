---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Valida las specs SDD del proyecto o de una feature
argument-hint: "[carpeta de la feature] [--fase spec|plan|tareas|implementar]"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Argumentos: $ARGUMENTS

1. Ejecuta `validar_spec.py` con los argumentos (sin argumentos, sobre la raíz del proyecto para validar todas las features).
2. Muestra los errores y avisos agrupados por feature y propone cómo corregir cada uno; no modifiques archivos sin confirmación del usuario.
