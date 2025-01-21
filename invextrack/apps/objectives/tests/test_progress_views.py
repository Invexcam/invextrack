from django.test import TestCase
from django.urls import reverse

class ProgressViewTests(TestCase):
    def test_progress_view(self):
        response = self.client.get(reverse('progress-list'))
        self.assertEqual(response.status_code, 200)