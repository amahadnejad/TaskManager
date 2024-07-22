from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task
from .forms import TaskForm


@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-status')

    return render(request, 'tasks/task_list.html', context={
        'tasks': tasks,
    })


@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task Has SuccessFully Created!")
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_create.html', {'form': form})


@login_required
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.warning(request, "Task Has SuccessFully Updated!")
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_update.html', {'form': form})


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.error(request, "Task Has SuccessFully Deleted!")
        return redirect('task_list')

    return render(request, 'tasks/task_delete.html', {'task': task})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def task_finish_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if task.status == 'p':  # If the task is pending
        task.status = 'd'  # Mark as completed
    elif task.status == 'd':  # If the task is completed
        task.status = 'p'  # Mark as pending

    task.save()
    return redirect('task_list')
