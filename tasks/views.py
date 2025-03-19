from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .services import calculate_priority
from django.contrib.auth.decorators import login_required
import datetime
import json
from django.contrib import messages
from django.http import JsonResponse
from .services import update_task_priorities

@login_required
def update_priorities_view(request):
    update_task_priorities()
    messages.success(request, "✅ Ülesannete prioriteedid on uuendatud!")
    return redirect('task_list')

def toggle_dark_mode(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session['dark_mode'] = data.get("dark_mode", False)
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/delete_task.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST['title']
        task.due_date = datetime.datetime.strptime(request.POST['due_date'], "%Y-%m-%d").date()
        task.complexity = int(request.POST['complexity'])
        task.frequency = int(request.POST['frequency'])

        task.priority = calculate_priority(task)  # AI uuendab prioriteedi
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/home.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        due_date_str = request.POST['due_date']
        
        # Konverteeri string kuupäevaks
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        
        complexity = int(request.POST['complexity'])
        frequency = int(request.POST['frequency'])

        task = Task.objects.create(
            user=request.user,
            title=title,
            due_date=due_date,
            complexity=complexity,
            frequency=frequency
        )

        task.priority = calculate_priority(task)  # AI arvutab prioriteedi
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/add_task.html')