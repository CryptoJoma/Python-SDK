
import requests
from .config import API_BASE_URL, API_KEY

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

    def get(self, endpoint):
        response = requests.get(f'{self.base_url}{endpoint}', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f'{self.base_url}{endpoint}', json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
