# Estructura propuesta: Java fullstack (Spring Boot + Thymeleaf)

Un solo módulo que sirve vistas HTML y, opcionalmente, una API REST. Alternativas con la misma base: Vaadin o JSF.

```
src/main/java/com/empresa/<proyecto>/
├── web/           # controladores de vistas (devuelven plantillas)
├── api/           # controladores REST (opcional, integraciones)
├── service/ (+ impl/)  repository/  model/entity/  dto/  mapper/
├── config/  security/  exception/  util/
src/main/resources/
├── templates/ (layouts, fragments, pages)
├── static/ (css, js, images)
└── db/migration/
src/test/java/... (web, api, service)
docker/  scripts/
```

## Reglas
- `web` y `api` comparten `service`; las vistas nunca acceden a repositorios.
- Las plantillas usan `layouts` + `fragments`; sin lógica de negocio en Thymeleaf.
- Los controladores usan DTO/ViewModel, no entidades.
- Documentación: backend en `Documentacion/backend`, UI en `Documentacion/frontend`.
