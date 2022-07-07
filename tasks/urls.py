from django.urls import path
from . import views
urlpatterns =[
    path('home', views.HomeView.as_view(), name='home'),
    path('tasks', views.TaskView.as_view(), name='tasks'),
    path('tasks_create', views.TasksCreateView.as_view(), name='tasks_create'),
    path('tasks_list', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks_detail/<int:pk>', views.TaskDetailView.as_view(), name='tasks_detail'),
    path('tasks_update/<int:pk>', views.TaskUpdateView.as_view(), name='tasks_update'),
    path('tasks_delete/<int:pk>', views.TaskDeleteView.as_view(), name='tasks_delete'),
]