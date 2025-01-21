from django.test import TestCase
from .models import User

class UserCreationTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertIsNotNone(user.id)