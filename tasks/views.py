from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from datetime import datetime

from tasks.models import Tasks

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

class TasksCreateView(CreateView):
    model = Tasks
    fields = ['title', 'description']
    template_name = 'tasks/task_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        context['now'] = datetime.now()
        return context
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return '/home'

class TaskListView(ListView):
    model = Tasks
    context_object_name= 'tasks'
    template_name = 'tasks/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List'
        context['now'] = datetime.now()
        return context