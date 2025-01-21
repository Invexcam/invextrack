from django.test import TestCase
from .models import Integration

class IntegrationTest(TestCase):
    def test_create_integration(self):
        integration = Integration.objects.create(name='Test Service', api_key='abcd1234')
        self.assertIsNotNone(integration.id)