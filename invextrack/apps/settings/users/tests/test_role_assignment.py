from django.test import TestCase
from django.contrib.auth.models import Group
from ..models import User
from ..services import assign_role

class RoleAssignmentTests(TestCase):
    def test_assign_role(self):
        user = User.objects.create_user(username='testuser', password='password')
        role = Group.objects.create(name='Test Role')
        assign_role(user, role)
        self.assertIn(role, user.groups.all())