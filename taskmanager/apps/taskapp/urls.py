from django.urls import path
from . import views

app_name = "taskapp"

urlpatterns = [
    path('', views.homepage, name="homePage"),
    path('task-create', views.taskcreate, name="newTask"),
    path("task-edit/<int:task_id>/", views.taskedit, name="taskEdit"),
    path("task-delete/<int:task_id>/", views.taskdelete, name="taskDelete"),
]