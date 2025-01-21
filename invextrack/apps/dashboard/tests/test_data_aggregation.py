from django.test import TestCase
from ..services.data_aggregation import aggregate_data

class DataAggregationTests(TestCase):
    def test_aggregate_data(self):
        data = aggregate_data()
        self.assertIsInstance(data, dict)