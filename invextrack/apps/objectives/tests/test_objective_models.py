from django.test import TestCase
from ..models.objective import Objective

class ObjectiveModelTests(TestCase):
    def test_objective_creation(self):
        objective = Objective.objects.create(title='Test Objective', description='Description', start_date='2023-01-01', end_date='2023-12-31')
        self.assertEqual(objective.title, 'Test Objective')