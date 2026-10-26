# Estructura propuesta: Python / FastAPI (backend API)

```
app/
├── api/v1/endpoints/  # routers por recurso
├── core/              # configuración, seguridad, logging
├── db/                # sesión, base declarativa
├── models/            # modelos ORM
├── schemas/           # esquemas Pydantic
├── services/          # lógica de negocio
├── repositories/      # acceso a datos
└── utils/
migrations/            # Alembic
tests/ (unit, integration)
docker/  scripts/
```

## Reglas
- Dependencias: `endpoints → services → repositories → models`.
- Los endpoints validan con `schemas` y no contienen lógica de negocio.
- Configuración por variables de entorno (`pydantic-settings`); `.env` fuera del repo.
- Archivos `snake_case.py`; dependencias fijadas (`requirements.txt` o `pyproject.toml`).
- Tests con `pytest`, espejando la estructura de `app/`.
