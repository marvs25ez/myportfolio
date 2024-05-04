from django.views.generic import TemplateView

class homePageview(TemplateView):
    template_name = "home.html"

class aboutPageview(TemplateView):
    template_name = "about.html"


class contactPageview(TemplateView):
    template_name = "contact.html"
