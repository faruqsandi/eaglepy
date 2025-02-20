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

    def get_library_history(self):
        url = f"{self.base_url}/api/library/history"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error: {error}")
            return None

    def get_library_icon(self, library_path):
        """Obtain the icon URL of the specified library."""
        from urllib.parse import urlencode

        params = {"libraryPath": library_path}
        query_string = urlencode(params)
        url = f"{self.base_url}/api/library/icon?{query_string}"

        return url  # Returns the URL of the icon, which can be used to fetch the image
