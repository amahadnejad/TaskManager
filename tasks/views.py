from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Task


@login_required
def task_list_view(request):
    # Get the tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user)

    return render(request, 'tasks/task_list.html', context={
        'tasks': tasks,
    })
