from django.db import models
from .task import Task

class Notification(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()
    notify_at = models.DateTimeField()

    def __str__(self):
        return self.message