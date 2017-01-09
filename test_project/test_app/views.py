from django.views.generic import TemplateView


class TestStaticView(TemplateView):
    template_name = 'index.html'
