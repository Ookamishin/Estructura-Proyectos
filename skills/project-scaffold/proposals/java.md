# Estructura propuesta: Java / Spring Boot (backend API)

Capas por paquete (`com.empresa.<proyecto>`).

```
src/main/java/com/empresa/<proyecto>/
├── config/        # beans y configuración
├── controller/    # REST, solo HTTP
├── dto/           # request/response
├── exception/     # excepciones y @ControllerAdvice
├── mapper/        # entidad <-> DTO
├── model/entity/  # entidades JPA
├── repository/    # acceso a datos
├── security/
├── service/ (+ impl/)  # lógica de negocio
└── util/
src/main/resources/db/migration/   # Flyway/Liquibase
src/test/java/...  (controller, service, repository)
docker/  scripts/
```

## Reglas
- Dependencias: `controller → service → repository`; nunca al revés.
- Los controladores no exponen entidades, solo DTO.
- La interfaz de servicio vive en `service/`, su implementación en `service/impl/`.
- Un archivo máx. 400 líneas; clases `PascalCase`, paquetes en minúsculas.
- Perfiles en `application-{perfil}.yml`; sin secretos en el repo.
