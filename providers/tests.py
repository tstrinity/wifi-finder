'''
 Basic coverege test
'''

from django.test import TestCase
from django.test.client import Client


class ResponseTest(TestCase):
    def test_providers_response(self):
        c = Client()
        response = c.get('/providers/','')
        self.assertEqual(response.status_code, 200)

    def test_getAllProviders_ajax_post(self):
        c = Client()
        response = c.post('/providers/getAllProviders', {})
        self.assertEqual(response.status_code, 200)
