from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
import json

def homepage(request):
    Tasks = Task.objects.all()
    return render(request, "taskmanager/index.html", {
        "Tasks": Tasks,
    })

@csrf_exempt
def taskcreate(request):
    Users = User.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:homePage")
    else:
        form = TaskForm()
    return render(request, "taskmanager/task-create.html", {
        'form': form,
        'Users': Users
    })

@csrf_exempt
def taskedit(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("main:homePage")
    else:
        form = TaskForm(instance=task)
    return render(request, "taskmanager/task-edit.html", {
        'form': form,
    })

@csrf_exempt
def taskdelete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect("main:homePage")
