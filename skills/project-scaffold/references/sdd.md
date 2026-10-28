# Spec-Driven Development (SDD)

La especificación es la fuente de verdad: primero se acuerda **qué** y **por qué**, luego **cómo**, y solo al final se escribe código. El código se deriva de la spec y se valida contra ella; si cambia el comportamiento, primero cambia la spec.

## Estructura en el proyecto
```
Documentacion/specs/
├── README.md               # esta guía
├── constitucion.md         # principios no negociables del proyecto
├── _plantillas/            # spec.md, plan.md, tareas.md
└── NNN-nombre-feature/     # una carpeta por feature (001-login, 002-reportes…)
    ├── spec.md             # qué y por qué (sin tecnología)
    ├── plan.md             # cómo: arquitectura, datos, contratos, riesgos
    └── tareas.md           # pasos pequeños, ordenados y verificables
```

## Flujo
| Fase | Entregable | Puerta para avanzar |
|---|---|---|
| 0. Constitución | `constitucion.md` (una vez por proyecto) | Principios aprobados por el equipo |
| 1. Especificar | `spec.md` | Sin `[POR ACLARAR]`; criterios de aceptación revisados por negocio |
| 2. Aclarar | Preguntas resueltas dentro de `spec.md` | Cada ambigüedad tiene respuesta registrada |
| 3. Planear | `plan.md` | Cumple la constitución; contratos y modelo de datos definidos |
| 4. Tareas | `tareas.md` | Cada tarea referencia un requisito y tiene verificación |
| 5. Implementar | Código + pruebas | Pruebas de los criterios de aceptación en verde |
| 6. Validar | Spec actualizada, estado `Implementada` | Spec, plan y código coinciden |

Para cambios triviales (typos, ajustes de estilo, bugs de una línea) no hace falta spec; para todo lo que cambie comportamiento, sí.

## Herramientas
Con el plugin `estructura-proyectos` (skill `project-scaffold`):
- `scripts/nueva_spec.py --nombre "<feature>"` crea `NNN-feature/` con las plantillas y la registra en el índice.
- `scripts/validar_spec.py <carpeta> --fase spec|plan|tareas|implementar` comprueba las puertas antes de avanzar.
- En Claude Code: `/sdd-especificar`, `/sdd-aclarar`, `/sdd-planear`, `/sdd-tareas`, `/sdd-implementar`, `/sdd-validar`.

## Buenas prácticas
**Spec (`spec.md`)**
- Describe el problema, usuarios y resultado esperado; nada de frameworks, tablas ni endpoints (eso va en el plan).
- Historias de usuario priorizadas (P1, P2, P3); cada una entregable y probable por separado.
- Requisitos numerados (`RF-001`, `RNF-001`) y atómicos: uno por línea, verificable, sin «etc.» ni «rápido» sin cifra.
- Criterios de aceptación en formato **Dado / Cuando / Entonces** o **EARS** (`CUANDO <evento> EL SISTEMA DEBE <respuesta>`).
- Declara explícitamente lo que queda **fuera de alcance**.
- Marca toda duda con `[POR ACLARAR: pregunta]`; no inventes supuestos. Si se asume algo, regístralo en «Supuestos».
- Criterios de éxito medibles y agnósticos de tecnología (p. ej. «el 95 % de búsquedas responde en < 1 s»).

**Plan (`plan.md`)**
- Contrasta cada decisión con la constitución; documenta excepciones con justificación.
- Define modelo de datos, contratos (OpenAPI, eventos, interfaces) y su ubicación en `Documentacion/<tipo>/api` o `base-de-datos`.
- Decisiones relevantes → ADR en `Documentacion/<tipo>/decisiones/NNNN-titulo.md`, enlazado desde el plan.
- Incluye riesgos, estrategia de pruebas y plan de rollback.
- Prefiere lo simple: no agregues capas, librerías ni proyectos que la spec no exija.

**Tareas (`tareas.md`)**
- Pequeñas (≤ medio día), con identificador (`T001`), requisito que cubren y criterio de terminado.
- Orden: contratos y pruebas primero (test-first), luego implementación, luego integración.
- Marca con `[P]` las tareas paralelizables (archivos distintos, sin dependencias).
- Agrupadas por historia para poder entregar P1 sin esperar a P2.

**Ciclo de vida**
- Las specs se versionan en git junto al código; un PR referencia su spec (`specs/003-…`).
- Estados: `Borrador` → `Aprobada` → `En implementación` → `Implementada` (o `Obsoleta`).
- Un cambio de comportamiento posterior actualiza la spec existente (con entrada en su historial) o crea una nueva que la reemplace; nunca dejes la spec desalineada del código.
- Revisión en pareja de la spec antes del plan: es más barato corregir un párrafo que un módulo.

**Con agentes de IA**
- Dale al agente la spec y el plan como contexto, no solo el prompt; pídele que trabaje tarea por tarea y marque las completadas.
- El agente no debe resolver `[POR ACLARAR]` por su cuenta: pregunta al usuario.
- Revisa el código generado contra los criterios de aceptación, no contra la intuición.

## Antipatrones
- Spec escrita después del código para «cumplir».
- Mezclar el cómo en la spec («usar Redis», «tabla `usuarios`»).
- Requisitos no verificables («intuitivo», «escalable») sin métrica.
- Tareas gigantes sin criterio de terminado o sin vínculo a requisitos.
- Specs que nadie actualiza tras el merge.
