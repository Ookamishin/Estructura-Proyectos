# Estructura-Proyectos

Este repositorio contiene la skill `project-scaffold` (`skills/project-scaffold/`), que crea proyectos con estructura de directorios estandarizada y carpeta `Documentacion`.

- Cuando el usuario pida crear o estandarizar un proyecto (Angular, Vue, React, Java, Python, Node, .NET), lee `skills/project-scaffold/SKILL.md` y sigue su flujo.
- Pregunta primero lo que falte: tipo (backend, frontend, ambos o fullstack), stack, nombre y ruta.
- Crea la estructura solo con `python3 skills/project-scaffold/scripts/scaffold.py` (en Windows: `python` o `py`); no crees directorios a mano.
- Toda documentación generada va dentro de `Documentacion/backend` o `Documentacion/frontend`.
- Para cambiar una estructura, edita juntos `structures/<stack>.dirs` y `proposals/<stack>.md`.
