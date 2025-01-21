from django.test import TestCase
from ..models.task import Task

class TaskModelTests(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(name='Test Task', description='Description', due_date='2023-01-01')
        self.assertEqual(task.name, 'Test Task')