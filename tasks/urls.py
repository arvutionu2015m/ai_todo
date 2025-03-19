from django.urls import path
from .views import task_list, add_task, edit_task, delete_task, toggle_dark_mode, update_priorities_view

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('toggle-dark-mode/', toggle_dark_mode, name='toggle_dark_mode'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),  # Lisa edit_task URL
    path('delete/<int:task_id>/', delete_task, name='delete_task'),  # Lisa delete_task URL
    path('update-priorities/', update_priorities_view, name='update_priorities'),
]