# VizDoom LiveView Demo

Integration demo of VizDoom with Django-LiveView for real-time game visualization.

## Demo Video

Watch the demo in action: [VizDoom Django-LiveView Demo](https://en.andros.dev/media/blog/2025/12/doom-django-liveview.mp4)

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
