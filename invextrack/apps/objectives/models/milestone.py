from django.db import models

class Milestone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.name