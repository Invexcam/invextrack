from django.test import TestCase
from django.urls import reverse

class TaskViewTests(TestCase):
    def test_task_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)