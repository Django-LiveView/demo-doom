from django.views.generic import TemplateView


class DoomPixelView(TemplateView):
	template_name = "doom_viewer.html"
