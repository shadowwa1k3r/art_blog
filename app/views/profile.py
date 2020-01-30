from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class AuthPageView(TemplateView):
    template_name = 'auth/sign-in.html'