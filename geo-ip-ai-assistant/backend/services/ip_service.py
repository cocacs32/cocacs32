import requests

class IPService:
    def __init__(self):
        self.api_url = 'https://ipapi.co/'

    def get_ip_details(self, ip_address):
        response = requests.get(f'{self.api_url}{ip_address}/json/')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_ip_location(self, ip_address):
        details = self.get_ip_details(ip_address)
        if details:
            return {'city': details.get('city'), 'region': details.get('region'), 'country': details.get('country')}
        else:
            return None

# Example usage:
# ip_service = IPService()
# print(ip_service.get_ip_location('8.8.8.8'))