# VizDoom LiveView Demo

Demo de integración de VizDoom con Django-LiveView para visualización en tiempo real del juego.

## Cómo levantar el proyecto

1. Asegúrate de tener Docker y Docker Compose instalados

2. Levanta los servicios:
```bash
docker-compose up --build
```

3. Accede a la aplicación en tu navegador:
```
http://localhost:8001
```

## Requisitos

- Docker
- Docker Compose

## Servicios

- **Web**: Aplicación Django con LiveView (puerto 8001)
- **Redis**: Cache y mensajería para Django-LiveView (puerto 6379)
