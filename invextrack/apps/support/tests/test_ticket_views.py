from django.test import TestCase
from django.urls import reverse

class TicketViewTests(TestCase):
    def test_ticket_view(self):
        response = self.client.get(reverse('ticket-list'))
        self.assertEqual(response.status_code, 200)