# Estructura propuesta: React (frontend)

TypeScript, organización por *features*.

```
public/
src/
├── app/
│   ├── providers/   # contexto global, tema, query client
│   ├── router/
│   └── store/
├── assets/
├── components/ui/   # primitivos genéricos
├── features/        # un directorio por dominio (components, hooks, api, types)
├── hooks/           # hooks genéricos
├── layouts/
├── pages/           # una página por ruta, solo composición
├── services/api/    # cliente HTTP base
├── lib/             # wrappers de librerías externas
├── types/
├── utils/
└── styles/
tests/ (unit, e2e)
```

## Reglas
- Una feature no importa de otra feature; lo compartido va a `components/ui`, `hooks` o `lib`.
- Las `pages` no contienen lógica de negocio; la delegan a `features`.
- Componentes en `PascalCase.tsx`, hooks `useNombre.ts`.
- Exporta cada feature por un `index.ts` (API pública).
