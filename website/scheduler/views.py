from django.views.generic import ListView
from .models import Practice

class PracticeListView(ListView):
    model = Practice
    template_name = "scheduler/list.html"
