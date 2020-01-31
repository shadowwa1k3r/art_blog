from django.views.generic import TemplateView


class MessagePageView(TemplateView):
    template_name = 'chat/messages.html'