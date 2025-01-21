from django.db import models
from .task import Task

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name