
import unittest
from licensechain.utils import setup_logging

class TestUtils(unittest.TestCase):
    def test_setup_logging(self):
        setup_logging()
        self.assertTrue(True)
