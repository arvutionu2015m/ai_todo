from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'priority', 'complexity', 'frequency')
    list_filter = ('priority', 'due_date')
