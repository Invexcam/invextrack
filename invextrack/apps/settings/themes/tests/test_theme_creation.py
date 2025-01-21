from django.test import TestCase
from ..models import Theme

class ThemeCreationTests(TestCase):
    def test_theme_creation(self):
        theme = Theme.objects.create(name='Test Theme', config={'key': 'value'})
        self.assertEqual(theme.name, 'Test Theme')