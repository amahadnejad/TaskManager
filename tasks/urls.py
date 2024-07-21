from django.urls import path

from .views import task_list_view, task_update_view, task_delete_view, task_create_view, task_finish_view

urlpatterns = [
    path('tasks/', task_list_view, name='task_list'),
    path('task/add/', task_create_view, name='task_create'),
    path('task/<int:pk>/edit/', task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),
    path('task/<int:pk>/finish/', task_finish_view, name='task_finish'),
]
