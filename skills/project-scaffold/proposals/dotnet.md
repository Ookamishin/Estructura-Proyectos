# Estructura propuesta: .NET (backend API)

Clean Architecture con cuatro proyectos y pruebas.

```
src/
├── <Proyecto>.Api/            # Controllers, Middleware, Extensions
├── <Proyecto>.Application/    # DTOs, Interfaces, Services, Validators, Mappings
├── <Proyecto>.Domain/         # Entities, Enums, Exceptions, Interfaces
└── <Proyecto>.Infrastructure/ # Persistence (Configurations, Migrations), Repositories, Services
tests/
├── <Proyecto>.UnitTests/
└── <Proyecto>.IntegrationTests/
docker/  scripts/
```

## Reglas
- Referencias: `Api → Application → Domain`; `Infrastructure → Application`; `Domain` no depende de nada.
- Los controladores usan DTO, nunca entidades.
- Interfaces de repositorios en `Domain`/`Application`, implementación en `Infrastructure`.
- Registro de dependencias por proyecto vía métodos de extensión (`AddApplication`, `AddInfrastructure`).
- Clases `PascalCase`; un tipo por archivo.
