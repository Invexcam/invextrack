from django.test import TestCase
from .models import Theme

class ThemeTest(TestCase):
    def test_theme_creation(self):
        theme = Theme.objects.create(name='Dark Mode', color_scheme={'background': 'black', 'text': 'white'})
        self.assertIsNotNone(theme.id)