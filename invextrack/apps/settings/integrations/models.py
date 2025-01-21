from django.db import models

class Integration(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)