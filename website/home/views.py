from django.shortcuts import render
from django.views.generic import TemplateView

from scheduler.models import Practice, Event

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Supplement additional data to frontend html for calendar
        context["event_list"] = Event.objects.all()
        context["practice_list"] = Practice.objects.all()
        return context
    