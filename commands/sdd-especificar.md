---
# NOTA: formato de comando específico de Claude Code (Markdown + frontmatter, $ARGUMENTS).
# Para usarlo con otra IA hay que adaptarlo a su formato de comandos/prompts
# (p. ej. Gemini CLI usa .toml con {{args}}; OpenCode y Codex usan .md con su propia carpeta).
# Ver la sección "Comandos SDD" del README.md.
description: Crea una feature SDD nueva y redacta su spec.md (qué y por qué)
argument-hint: "<nombre de la feature y descripción>"
---

Invoca la skill `project-scaffold` y sigue su sección «Spec-Driven Development (SDD)» y `references/sdd.md`. Los scripts están en la carpeta `scripts/` de la skill (en Windows usa `python` o `py`).

Feature solicitada: $ARGUMENTS

1. Si falta el nombre o la descripción de la feature, pregúntalos al usuario.
2. Si no existe `Documentacion/specs/constitucion.md`, avisa al usuario y propón completarla primero.
3. Crea la carpeta con `nueva_spec.py --nombre "<nombre>" --ruta <raíz del proyecto>` (no la crees a mano).
4. Llena `spec.md`: problema, historias priorizadas con criterios Dado/Cuando/Entonces o EARS, requisitos `RF-/RNF-` ligados a historias, casos borde, fuera de alcance y criterios de éxito medibles. Sin tecnología.
5. Toda duda va como `[POR ACLARAR: pregunta]`; no inventes supuestos.
6. Ejecuta `validar_spec.py <carpeta de la feature> --fase spec` y muestra el resultado.
7. Responde con la ruta creada, un resumen de la spec y la lista de `[POR ACLARAR]` (sugiere `/sdd-aclarar`).
