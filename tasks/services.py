import datetime
from .models import Task

def calculate_priority(task):
    """
    Arvutab ülesande prioriteedi, arvestades tähtaega, keerukust ja sagedust.
    """
    days_left = (task.due_date - datetime.date.today()).days
    urgency_score = max(1, 10 - days_left)  # Vähem jäänud päevi = suurem prioriteet
    complexity_score = task.complexity * 2  # Keerukus suurendab kaalu
    frequency_score = max(1, 7 - task.frequency)  # Harvem ülesanne = suurem prioriteet

    total_score = urgency_score + complexity_score + frequency_score

    if total_score > 15:
        return 'High'
    elif total_score > 8:
        return 'Medium'
    else:
        return 'Low'

def update_task_priorities():
    """
    Värskendab kõigi ülesannete prioriteedi vastavalt AI loogikale.
    """
    tasks = Task.objects.all()
    for task in tasks:
        task.priority = calculate_priority(task)
        task.save()
