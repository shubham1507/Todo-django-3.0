from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

# Create your views here.


def index(request):

    qs = Task.objects.all()

    f = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task': qs, 'form': f}
    return render(request, 'task/list.html', context)


def update_task(request, pk):

    item = Task.objects.get(id=pk)

    form = TaskForm(instance=item)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'task/update_task.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'task/delete.html', context)
