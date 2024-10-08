
from .api_client import APIClient
from .exceptions import LicenseChainAPIError

class LicenseValidator:
    def __init__(self):
        self.client = APIClient()

    def validate_license(self, license_key):
        try:
            response = self.client.get(f'licenses/{license_key}/validate')
            return response
        except Exception as e:
            raise LicenseChainAPIError(f'Error validating license: {e}')
