from django.test import TestCase
from django.urls import reverse

class EndpointTests(TestCase):
    def test_task_endpoint(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)