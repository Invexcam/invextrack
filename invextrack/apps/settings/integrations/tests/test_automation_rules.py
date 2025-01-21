from django.test import TestCase
from ..models import Integration

class AutomationRulesTests(TestCase):
    def test_integration_creation(self):
        integration = Integration.objects.create(name='Test Integration', config={'key': 'value'})
        self.assertEqual(integration.name, 'Test Integration')