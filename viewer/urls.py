from django.urls import path

from .views import DoomPixelView

urlpatterns = [
	path("", DoomPixelView.as_view(), name="doom_viewer"),
]
