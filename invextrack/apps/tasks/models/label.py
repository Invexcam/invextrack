from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name