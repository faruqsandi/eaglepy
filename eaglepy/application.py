import requests


class Application:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_info(self):
        url = f"{self.base_url}/api/application/info"
        response = requests.get(url)
        return response.json()
