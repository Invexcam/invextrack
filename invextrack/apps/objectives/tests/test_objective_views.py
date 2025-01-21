from django.test import TestCase
from django.urls import reverse

class ObjectiveViewTests(TestCase):
    def test_objective_view(self):
        response = self.client.get(reverse('objective-list'))
        self.assertEqual(response.status_code, 200)