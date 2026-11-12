# Estructura-Proyectos

Este repositorio contiene la skill `project-scaffold` (`skills/project-scaffold/`), que crea proyectos con estructura de directorios estandarizada y carpeta `Documentacion`.

- Cuando el usuario pida crear o estandarizar un proyecto (Angular, Vue, React, Java, Python, Node, .NET), lee `skills/project-scaffold/SKILL.md` y sigue su flujo.
- Pregunta primero lo que falte: tipo (backend, frontend, ambos o fullstack), stack, metodología (SDD, ODD, ambas o ninguna), nombre y ruta.
- Crea la estructura solo con `python3 skills/project-scaffold/scripts/scaffold.py` (en Windows: `python` o `py`); no crees directorios a mano.
- Toda documentación generada va dentro de `Documentacion/backend` o `Documentacion/frontend`; las specs de features (SDD) van en `Documentacion/specs/NNN-feature/`.
- Para features o cambios de comportamiento, aplica Spec-Driven Development según `skills/project-scaffold/references/sdd.md`: spec → plan → tareas → implementación. Crea cada feature con `scripts/nueva_spec.py` y valida con `scripts/validar_spec.py` antes de pasar de fase.
- Si el proyecto usa ODD (`Documentacion/odd/`), clasifica el trabajo (small/sustancial) según `skills/project-scaffold/references/odd.md`; los sustanciales se registran con `scripts/nueva_tarea.py` en `Documentacion/odd/tasks/NNN-slug.md`. El usuario decide la metodología; no impongas una.
- Para cambiar una estructura, edita juntos `structures/<stack>.dirs` y `proposals/<stack>.md`.
