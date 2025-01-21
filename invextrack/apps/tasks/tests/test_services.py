from django.test import TestCase
from ..services.task_helper import create_task

class TaskServiceTests(TestCase):
    def test_create_task(self):
        task = create_task('Test Task', 'Description', '2023-01-01')
        self.assertEqual(task.name, 'Test Task')