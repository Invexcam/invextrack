from django.test import TestCase
from ..models.project import Project

class ProjectModelTests(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(name='Test Project', description='Description', start_date='2023-01-01', end_date='2023-12-31')
        self.assertEqual(project.name, 'Test Project')