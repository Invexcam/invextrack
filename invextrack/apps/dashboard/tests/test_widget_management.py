from django.test import TestCase
from ..services.widget_management import create_widget

class WidgetManagementTests(TestCase):
    def test_create_widget(self):
        widget = create_widget('Test Widget', 'Description', {'key': 'value'})
        self.assertEqual(widget.title, 'Test Widget')