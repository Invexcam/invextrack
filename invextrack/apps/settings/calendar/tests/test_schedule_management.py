from django.test import TestCase
from ..services import create_event

class ScheduleManagementTests(TestCase):
    def test_create_event(self):
        event = create_event('Test Event', 'Description', '2023-01-01T10:00:00Z', '2023-01-01T12:00:00Z')
        self.assertEqual(event.title, 'Test Event')