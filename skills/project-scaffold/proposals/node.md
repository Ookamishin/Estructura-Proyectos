# Estructura propuesta: Node.js (backend API)

TypeScript; válida para Express, Fastify o adaptable a NestJS.

```
src/
├── config/        # variables de entorno validadas
├── controllers/   # manejan req/res
├── routes/        # definición de rutas
├── services/      # lógica de negocio
├── repositories/  # acceso a datos
├── models/
├── middlewares/   # auth, errores, logging
├── validators/    # esquemas (zod/joi)
├── utils/
└── types/
migrations/
tests/ (unit, integration)
docker/  scripts/
```

## Reglas
- Dependencias: `routes → controllers → services → repositories`.
- Validar toda entrada en `validators`; manejo de errores centralizado en un middleware.
- Archivos `kebab-case` o `camelCase` (elegir uno y mantenerlo); `index.ts` solo para re-exportar.
- Sin secretos en el repo; `.env.example` versionado.
