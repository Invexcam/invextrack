from django.test import TestCase
from django.urls import reverse

class MilestoneViewTests(TestCase):
    def test_milestone_view(self):
        response = self.client.get(reverse('milestone-list'))
        self.assertEqual(response.status_code, 200)