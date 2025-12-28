from django.apps import AppConfig


class ViewerConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "viewer"

	def ready(self):
		"""Import liveview handlers when app is ready"""
		from viewer.liveview_components import doom_streamer  # noqa
