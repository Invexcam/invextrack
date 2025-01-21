from django.db import models

class Widget(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    config = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title