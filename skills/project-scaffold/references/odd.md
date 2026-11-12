# Organic Driven Development (ODD)

Flujo ligero: el esfuerzo de documentación es proporcional al riesgo. No todo cambio merece spec.

## Estructura en el proyecto
```
Documentacion/odd/
├── README.md             # esta guía
├── _plantillas/tarea.md  # plantilla del registro único
└── tasks/NNN-slug.md     # un archivo por trabajo sustancial (Specs / Tasks / Verificación / Log)
```

## Clasificación (test de recuperación)
- **Small**: una sesión nueva recupera intención, estado y siguiente paso con la petición original + `git diff`, y el riesgo es contenido. → Implementa, prueba de regresión si hay oráculo determinista, commit. Sin tarea ni documentación.
- **Sustancial**: falla ese test o toca contrato público/API, autenticación o permisos, datos persistidos o esquema, operación irreversible, release o seguridad. → Crea `tasks/NNN-slug.md`.
- Si dudas, elige sustancial: un registro de más cuesta menos que perder el contexto.

## Trabajo sustancial
1. Crea la tarea con `scripts/nueva_tarea.py --nombre "<tarea>"` (numeración compartida con las specs SDD).
2. Redacta **Specs** (S1…), **Tasks** (T1…, cada una con su check) y la **Verificación** global.
3. Una unidad = un commit (≤ ~400 líneas); el mensaje cita `S1/T1` y el check ejecutado.
4. Anota en **Log** decisiones, fallos y el siguiente paso. Marca `[x]` al cerrar cada tarea y pon `Estado: Cerrada`.
5. Cierre: informa qué se ejecutó, qué falló y qué queda pendiente; sin salida del check no hay cierre.

## Reglas
- Un requisito vive en un solo sitio: no lo copies a issues, planes ni notas.
- Issues solo para lo diferido; CHANGELOG solo para lo enviado.
- Si el trabajo crece hasta necesitar spec formal, escala a SDD (`Documentacion/specs/`) y enlaza la tarea.
