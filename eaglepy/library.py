import requests


class Library:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_library_info(self) -> dict:
        """
        GET detailed information of the library currently running.

        Returns:
            dict: A dictionary containing details such as all folders, smart folders, tag groups, quick access, etc.
        """
        url = f"{self.base_url}/api/library/info"
        response = requests.get(url)
        return response.json()

    def switch_library(self, library_path: str) -> dict:
        """
        POST switch the library currently opened by Eagle.

        Parameters:
            library_path (str): The path of the library to switch to.

        Returns:
            dict: A dictionary containing the response from the server.
        """
        url = f"{self.base_url}/api/library/switch"
        data = {"libraryPath": library_path}
        response = requests.post(url, json=data)
        return response.json()

    def get_library_history(self) -> dict:
        """
        GET the list of libraries recently opened by the application.

        Returns:
            dict: A dictionary containing the list of recently opened libraries.
        """
        url = f"{self.base_url}/api/library/history"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error: {error}")
            return None

    def get_library_icon(self, library_path: str) -> str:
        """
        GET the icon of the specified library.

        Parameters:
            library_path (str): The path of the library.

        Returns:
            str: The URL of the icon, which can be used to fetch the image.
        """
        from urllib.parse import urlencode

        params = {"libraryPath": library_path}
        query_string = urlencode(params)
        url = f"{self.base_url}/api/library/icon?{query_string}"

        return url  # Returns the URL of the icon, which can be used to fetch the image
