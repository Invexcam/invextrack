from django.db import models
from .ticket import Ticket

class Reply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]