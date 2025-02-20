import requests


class Application:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_info(self) -> dict:
        """
        GET Get detailed information on the Eagle App currently running.

        In most cases, this could be used to determine whether certain functions 
        are available on the user's device.

        Returns:
            dict: A dictionary containing the detailed information of the Eagle App.
        """
        url = f"{self.base_url}/api/application/info"
        response = requests.get(url)
        return response.json()
