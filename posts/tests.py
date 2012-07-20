'''
 Basic coverege test
'''


from django.test import TestCase
from django.test.client import Client


class ResponsePostTest(TestCase):
    def test_index_response(self):
        c = Client()
        response = c.get('/posts/','')
        self.assertEqual(response.status_code, 200)
