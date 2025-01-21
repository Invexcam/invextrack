from django.db import models
from .objective import Objective

class Progress(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    progress_date = models.DateField()
    progress_value = models.IntegerField()

    def __str__(self):
        return f"{self.objective.title} - {self.progress_value}%"