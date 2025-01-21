from django.test import TestCase
from .models import Event

class EventCreationTest(TestCase):
    def test_event_creation(self):
        event = Event.objects.create(title='Meeting', start_time='2025-01-14T10:00:00Z', end_time='2025-01-14T11:00:00Z')
        self.assertIsNotNone(event.id)