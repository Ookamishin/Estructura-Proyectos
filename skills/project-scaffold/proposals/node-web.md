# Estructura propuesta: Node fullstack (Next.js, App Router)

TypeScript. Para Nuxt (Vue) la lógica es análoga: `pages/`, `server/api/`, `components/`, `composables/`.

```
public/
src/
├── app/
│   ├── api/          # route handlers (backend)
│   ├── (auth)/       # rutas públicas
│   └── (main)/       # rutas protegidas
├── components/ (ui, features)
├── lib/  hooks/  types/  styles/
└── server/ (services, repositories, validators)   # solo se importa desde el servidor
prisma/
tests/ (unit, e2e)
docker/  scripts/
```

## Reglas
- Lo de `server/` nunca se importa desde componentes cliente.
- Los route handlers validan entrada y delegan en `server/services`.
- Componentes `PascalCase.tsx`; separar Server y Client Components explícitamente.
- Documentación: backend en `Documentacion/backend`, UI en `Documentacion/frontend`.
