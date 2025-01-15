from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Practice
from .forms import PracticeForm


class PracticeListView(ListView):
    model = Practice
    template_name = "scheduler/list.html"

class PracticeCreateView(CreateView):
    model = Practice
    template_name = "scheduler/form.html"
    form_class = PracticeForm
    success_url = reverse_lazy('scheduler:practice-all')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["practice_list"] = Practice.objects.all() 
        return context
    

class PracticeUpdateView(UpdateView):
    model = Practice
    template_name = "scheduler/form.html"
    form_class = PracticeForm
    success_url = reverse_lazy('scheduler:practice-all')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["practice_list"] = Practice.objects.all() 
        return context

class PracticeDeleteView(DeleteView):
    model = Practice
    template_name = "scheduler/confirm_delete.html"
    success_url = reverse_lazy('scheduler:practice-all')
