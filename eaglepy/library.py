import requests

class Library:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_library_info(self):
        url = f"{self.base_url}/api/library/info"
        response = requests.get(url)
        return response.json()

    def switch_library(self, library_path):
        url = f"{self.base_url}/api/library/switch"
        data = {"libraryPath": library_path}
        response = requests.post(url, json=data)
        return response.json()
