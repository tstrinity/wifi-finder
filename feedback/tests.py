from django.test import TestCase
from django.test.client import Client


#testing if the feedback page is available
class ResponseTest(TestCase):
    def test_feedback_view(self):
        c = Client()
        response = c.get('/feedback/','')
        self.assertEqual(response.status_code, 200)
