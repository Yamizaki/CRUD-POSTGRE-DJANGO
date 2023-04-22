from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def lista_tareas(request):
    tasks= Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})

def create_task(request):
    task = Task(title=request.POST["title"], description=request.POST["description"])
    task.save()
    print(request.POST)
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/') 

def done_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = True
    task.save()
    return redirect('/tasks/') 