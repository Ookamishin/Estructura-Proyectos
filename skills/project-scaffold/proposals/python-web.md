# Estructura propuesta: Python fullstack (Django)

```
config/settings/     # base, dev, prod
apps/
├── core/  accounts/  # apps por dominio (modelos, vistas, urls)
└── api/              # endpoints REST (DRF) opcionales
templates/ (layouts, partials, pages)
static/ (css, js, images)
services/            # lógica de negocio fuera de las vistas
locale/  migrations/
tests/ (unit, integration)
docker/  scripts/
```

## Reglas
- Una app por dominio; las vistas delgadas llaman a `services/`.
- Las plantillas heredan de `layouts/`; fragmentos reutilizables en `partials/`.
- Configuración por entorno con variables; sin secretos en el repo.
- Documentación: backend en `Documentacion/backend`, UI en `Documentacion/frontend`.
