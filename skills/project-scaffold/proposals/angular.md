# Estructura propuesta: Angular (frontend)

Componentes standalone, organización por *features*.

```
src/
├── app/
│   ├── core/           # singleton de la app
│   │   ├── guards/
│   │   ├── interceptors/
│   │   ├── services/
│   │   └── models/
│   ├── shared/         # reutilizable, sin lógica de negocio
│   │   ├── components/ directives/ pipes/ utils/
│   ├── features/       # un directorio por módulo funcional (ej. usuarios/)
│   └── layouts/        # shells (principal, auth)
├── assets/ (images, i18n)
├── environments/
└── styles/
tests/e2e/
```

## Reglas
- `core` se importa una sola vez; `shared` nunca depende de `features`.
- Cada feature contiene sus `pages/`, `components/`, `services/`, `models/` y su archivo de rutas (lazy loading).
- Una feature no importa de otra: lo común sube a `shared` o `core`.
- Nombres: `nombre.component.ts`, `nombre.service.ts`, `kebab-case` en archivos.
- Pruebas unitarias junto al archivo (`*.spec.ts`); e2e en `tests/e2e`.
