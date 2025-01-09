from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Practice

class PracticeListView(ListView):
    model = Practice
    template_name = "scheduler/list.html"

class PracticeCreateView(CreateView):
    model = Practice
    fields = "__all__"
    template_name = "scheduler/form.html"

class PracticeUpdateView(UpdateView):
    model = Practice
    fields = "__all__"
    template_name = "scheduler/form.html"

class PracticeDeleteView(DeleteView):
    model = Practice
    template_name = "scheduler/delete_confirm.html"
