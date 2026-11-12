---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Genera el plan.md técnico de una spec aprobada
argument-hint: "[carpeta o número de la feature]"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Feature: $ARGUMENTS (si no se indica, usa la más reciente de `Documentacion/specs/`).

1. Ejecuta `validar_spec.py <carpeta> --fase plan`. Si hay errores, muéstralos y detente (sugiere `/sdd-aclarar`).
2. Lee `constitucion.md`, la spec y la estructura del proyecto (`Documentacion/**/estructura-*.md`).
3. Llena `plan.md`: resumen técnico, verificación contra cada principio de la constitución (justifica excepciones), contexto técnico, modelo de datos, contratos, estrategia de pruebas con cada `RF-` y su prueba, riesgos y rollback.
4. Las decisiones relevantes van como ADR en `Documentacion/<tipo>/decisiones/NNNN-titulo.md`; contratos y modelo de datos detallados en `api/` y `base-de-datos/`.
5. Prefiere la solución más simple que cumpla la spec. Pide al usuario que revise el plan antes de `/sdd-tareas`.
