"""
ASGI config for vizdoom_liveview project.
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from liveview.routing import get_liveview_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Get Django app first
django_asgi_app = get_asgi_application()

# Import liveview handlers AFTER Django setup
from viewer.liveview_components import doom_streamer  # noqa

application = ProtocolTypeRouter(
	{
		"http": django_asgi_app,
		"websocket": AllowedHostsOriginValidator(
			AuthMiddlewareStack(URLRouter(get_liveview_urlpatterns()))
		),
	}
)
