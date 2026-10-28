---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Resuelve con el usuario las dudas [POR ACLARAR] de una spec
argument-hint: "[carpeta o número de la feature]"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Feature: $ARGUMENTS (si no se indica, usa la más reciente de `Documentacion/specs/`).

1. Lee `spec.md` y lista los `[POR ACLARAR]` y las ambigüedades (requisitos sin métrica, historias sin criterio).
2. Pregunta al usuario, máximo 5 preguntas por ronda, con opciones cuando sea posible (AskUserQuestion).
3. Sustituye cada marca por la respuesta y regístrala en la tabla «Aclaraciones» con la fecha.
4. Ejecuta `validar_spec.py <carpeta> --fase plan`. Si solo falla el estado, pregunta al usuario si aprueba la spec y, si acepta, cambia el estado a `Aprobada`.
