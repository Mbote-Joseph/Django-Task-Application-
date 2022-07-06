from django.urls import path
from . import views
urlpatterns =[
    path('home', views.HomeView.as_view(), name='home'),
    path('tasks', views.TaskView.as_view(), name='tasks'),
    path('tasks_create', views.TasksCreateView.as_view(), name='tasks_create'),
    path('tasks_list', views.TaskListView.as_view(), name='tasks_list'),
]