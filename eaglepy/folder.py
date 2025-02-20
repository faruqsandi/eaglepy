import requests

class Folder:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_folder(self, folder_name):
        url = f"{self.base_url}/api/folder/create"
        data = {"folderName": folder_name}
        response = requests.post(url, json=data)
        return response.json()

    def rename_folder(self, folder_id, new_name):
        url = f"{self.base_url}/api/folder/rename"
        data = {"folderId": folder_id, "newName": new_name}
        response = requests.post(url, json=data)
        return response.json()

    def update_folder(self, folder_id, new_name, new_description, new_color):
        url = f"{self.base_url}/api/folder/update"
        data = {
            "folderId": folder_id,
            "newName": new_name,
            "newDescription": new_description,
            "newColor": new_color
        }
        response = requests.post(url, json=data)
        return response.json()

    def list_folders(self):
        url = f"{self.base_url}/api/folder/list"
        response = requests.get(url)
        return response.json()

    def list_recent_folders(self):
        url = f"{self.base_url}/api/folder/listRecent"
        response = requests.get(url)
        return response.json()
