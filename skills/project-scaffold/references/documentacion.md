# Carpeta Documentacion

```
Documentacion/
├── README.md                 # índice
├── specs/                    # SDD: README (guía), constitucion.md, _plantillas/, NNN-feature/
├── backend/
│   ├── estructura-<stack>.md # propuesta de directorios
│   ├── arquitectura/         # diagramas, capas, flujos
│   ├── api/                  # contratos, endpoints, OpenAPI
│   ├── base-de-datos/        # modelo, migraciones, diccionario
│   ├── decisiones/           # ADRs (NNNN-titulo.md)
│   ├── guias/                # instalación, configuración, contribución
│   ├── operaciones/          # despliegue, monitoreo, runbooks
│   └── pruebas/              # estrategia y reportes
└── frontend/
    ├── estructura-<stack>.md
    ├── arquitectura/
    ├── componentes/          # catálogo y convenciones
    ├── diseno-ui/            # guía de estilos, tokens
    ├── decisiones/
    ├── guias/
    └── pruebas/
```

Reglas: nombres en minúsculas con guiones, un tema por archivo, fecha y autor al inicio de cada documento, ADRs y specs numerados (ver `sdd.md`).
