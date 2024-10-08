
import unittest
from licensechain.license_validator import LicenseValidator

class TestLicenseValidator(unittest.TestCase):
    def test_validate_license(self):
        validator = LicenseValidator()
        self.assertRaises(Exception, validator.validate_license, 'invalid_license_key')
