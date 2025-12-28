# VizDoom LiveView Demo

Integration demo of VizDoom with Django-LiveView for real-time game visualization.

## How to run

1. Make sure you have Docker and Docker Compose installed

2. Start the services:
```bash
docker-compose up --build
```

3. Access the application in your browser:
```
http://localhost:8001
```

## Requirements

- Docker
- Docker Compose

## Services

- **Web**: Django application with LiveView (port 8001)
- **Redis**: Cache and messaging for Django-LiveView (port 6379)
