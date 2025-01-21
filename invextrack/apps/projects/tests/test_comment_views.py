from django.test import TestCase
from django.urls import reverse

class CommentViewTests(TestCase):
    def test_comment_view(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, 200)