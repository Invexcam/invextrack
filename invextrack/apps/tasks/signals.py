from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.task import Task

@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        # Logic to execute after a task is created
        pass