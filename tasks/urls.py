from django.urls import path
from . import views
urlpatterns =[
    path('home', views.HomeView.as_view(), name='home'),
    path('tasks', views.TaskView.as_view(), name='tasks'),
]