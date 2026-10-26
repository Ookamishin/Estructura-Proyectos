# Estructura propuesta: Vue 3 (frontend)

Composition API (`<script setup>`), Pinia y Vue Router.

```
public/
src/
├── assets/
├── components/
│   ├── common/      # componentes de negocio reutilizables
│   └── ui/          # primitivos (botón, input, modal)
├── composables/     # lógica reutilizable (useXxx)
├── layouts/
├── router/
├── stores/          # Pinia, un store por dominio
├── services/api/    # clientes HTTP
├── views/           # una vista por ruta
├── types/
├── utils/
└── plugins/
tests/ (unit, e2e)
```

## Reglas
- Las `views` componen componentes; no llaman a la API directamente (usan `services` vía `stores`/`composables`).
- Componentes en `PascalCase.vue`; composables `useNombre.ts`; stores `nombre.store.ts`.
- Estado global solo en `stores`; el estado local se queda en el componente.
- Pruebas unitarias en `tests/unit` espejando `src/`.
