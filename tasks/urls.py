from django.urls import path

from .views import task_list_view, task_update_view, task_delete_view

urlpatterns = [
    path('tasks/', task_list_view, name='task_list'),
    path('task/<int:pk>/edit/', task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),

]
