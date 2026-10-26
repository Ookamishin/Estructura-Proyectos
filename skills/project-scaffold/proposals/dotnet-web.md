# Estructura propuesta: .NET fullstack (ASP.NET Core MVC/Razor)

Un proyecto web con vistas y API, más capas de apoyo. Para Blazor, sustituye `Views/` por `Components/` y `Pages/`.

```
src/
├── <Proyecto>.Web/          # Controllers, Api, Views, ViewModels, Middleware, wwwroot
├── <Proyecto>.Application/  # DTOs, Interfaces, Services, Validators
├── <Proyecto>.Domain/       # Entities, Enums, Exceptions
└── <Proyecto>.Infrastructure/  # Persistence, Repositories
tests/ (UnitTests, IntegrationTests)
docker/  scripts/
```

## Reglas
- Referencias: `Web → Application → Domain`; `Infrastructure → Application`.
- Controladores MVC usan `ViewModels`; los de `Api/` usan DTO.
- Estáticos solo en `wwwroot`; un tipo por archivo, `PascalCase`.
- Documentación: backend en `Documentacion/backend`, UI en `Documentacion/frontend`.
