from django.shortcuts import redirect, render
from django.http import HttpResponse

from googlesearch import search as searchGoogle

from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    args = {'tasks': tasks, 'form': form}
    return render(request, 'task/list.html', args)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    args = {'form': form}
    return render(request, 'task/updateItem.html', args)


def delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    args = {'item': task}
    return render(request, 'task/delete.html', args)


def howTo(request):
    return render(request, 'task/howto.html')
