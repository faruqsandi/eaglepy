import requests
from typing import Optional, Dict


class Folder:
    def __init__(self, base_url: str):
        """
        Initialize the Folder class with the base URL for the API.

        :param base_url: The base URL for the API.
        """
        self.base_url = base_url

    def create_folder(self, folder_name: str, parent: Optional[str] = None) -> Dict:
        """
        Create a folder. The created folder will be put at the bottom of the folder list of the current library.

        :param folder_name: The name of the folder.
        :param parent: ID of the parent folder.
        :return: The response from the API as a dictionary.
        """
        url = f"{self.base_url}/api/folder/create"
        data = {"folderName": folder_name, "parent": parent}
        response = requests.post(url, json=data)
        return response.json()

    def rename_folder(self, folder_id: str, new_name: str) -> Dict:
        """
        Rename the specified folder.

        :param folder_id: The folder's ID.
        :param new_name: The new name of the folder.
        :return: The response from the API as a dictionary.
        """
        url = f"{self.base_url}/api/folder/rename"
        data = {"folderId": folder_id, "newName": new_name}
        response = requests.post(url, json=data)
        return response.json()

    def update_folder(self, folder_id: str, new_name: str, new_description: str, new_color: str) -> Dict:
        """
        Update the specified folder.

        :param folder_id: The folder's ID.
        :param new_name: The new name of the folder.
        :param new_description: The new description of the folder.
        :param new_color: The new color of the folder. Options are "red", "orange", "green", "yellow", "aqua", "blue", "purple", "pink".
        :return: The response from the API as a dictionary.
        """
        url = f"{self.base_url}/api/folder/update"
        data = {
            "folderId": folder_id,
            "newName": new_name,
            "newDescription": new_description,
            "newColor": new_color
        }
        response = requests.post(url, json=data)
        return response.json()

    def list_folders(self) -> Dict:
        """
        Get the list of folders of the current library.

        :return: The response from the API as a dictionary.
        """
        url = f"{self.base_url}/api/folder/list"
        response = requests.get(url)
        return response.json()

    def list_recent_folders(self) -> Dict:
        """
        Get the list of folders recently used by the user.

        :return: The response from the API as a dictionary.
        """
        url = f"{self.base_url}/api/folder/listRecent"
        response = requests.get(url)
        return response.json()
