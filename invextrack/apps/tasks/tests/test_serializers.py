from django.test import TestCase
from ..serializers.task_serializer import TaskSerializer
from ..models.task import Task

class TaskSerializerTests(TestCase):
    def test_task_serializer(self):
        task = Task.objects.create(name='Test Task', description='Description', due_date='2023-01-01')
        serializer = TaskSerializer(task)
        self.assertEqual(serializer.data['name'], 'Test Task')