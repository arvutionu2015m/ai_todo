from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Madal'),
        ('Medium', 'Keskmine'),
        ('High', 'Kõrge'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    complexity = models.IntegerField(default=1)  # 1-5 skaalal
    frequency = models.IntegerField(default=1)  # Kui tihti ülesanne esineb (1-7 päeva)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
