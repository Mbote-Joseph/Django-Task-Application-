from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.
class HomeView(TemplateView):
    template_name = 'tasks/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['now'] = datetime.now()
        return context
   
class TaskView(TemplateView):
    template_name = 'tasks/tasks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task'
        context['now'] = datetime.now()
        return context