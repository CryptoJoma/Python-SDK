
import unittest
from licensechain.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_get(self):
        client = APIClient()
        self.assertRaises(Exception, client.get, 'invalid_endpoint')
