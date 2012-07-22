"""
 Basic coverege test
"""


from django.test import TestCase
from django.test.client import Client


class ResponseTest(TestCase):

    def test_index_response(self):
        c = Client()
        response = c.get('/points/','')
        self.assertEqual(response.status_code, 200)


    def test_json_points_response(self):
        c = Client()
        response = c.post('/points/getAllPoints/',{'provider' : 'provider_doesnt_exist'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,'{"success": "no"}')