from ..models.notification import Notification

def create_reminder(task, message, notify_at):
    reminder = Notification.objects.create(task=task, message=message, notify_at=notify_at)
    return reminder

def delete_reminder(reminder_id):
    reminder = Notification.objects.get(id=reminder_id)
    reminder.delete()