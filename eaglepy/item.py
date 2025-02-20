import requests
from typing import Optional, List, Dict


class Item:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_item_from_url(
        self,
        url: str,
        name: str,
        website: Optional[str] = None,
        tags: Optional[List] = None,
        modification_time: Optional[int] = None,
        headers: Optional[dict] = None
    ) -> dict:
        """
        POST Add an image from an address to Eagle App. If you intend to add multiple items in a row, 
        we suggest you use /api/item/addFromURLs.

        Parameters:
        url (str): Required, the URL of the image to be added. Supports http, https, base64.
        name (str): Required, The name of the image to be added.
        website (str): The Address of the source of the image.
        tags (list): Tags for the image.
        modification_time (int): The creation date of the image. The parameter can be used to alter the image's sorting order in Eagle.
        headers (dict): Optional, customize the HTTP headers properties, this could be used to circumvent the security of certain websites.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/addFromURL"
        data = {
            "url": url,
            "name": name,
            "website": website,
            "tags": tags,
            "modificationTime": modification_time,
            "headers": headers
        }
        response = requests.post(api_url, json=data)
        return response.json()

    def add_items_from_urls(
        self,
        items: List[Dict[str, Optional[str]]],
        folder_id: Optional[str] = None
    ) -> dict:
        """
        POST Add multiple images from URLs to Eagle App.

        Parameters:
        items (list): The array object made up of multiple items. Each item should have the following structure:
            - url (str): Required, the URL of images to be added. Supports http, https, base64.
            - name (str): Required, The name of the images to be added.
            - website (str): The Address of the source of images.
            - annotation (str): The annotation for the images.
            - tags (list): Tags for the images.
            - modificationTime (int): The creation date of the images. The parameter can be used to alter the images' sorting order in Eagle.
            - headers (dict): Optional, customize the HTTP headers properties, this could be used to circumvent the security of certain websites.
        folder_id (str): If the parameter is defined, images will be added to the corresponding folder.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/addFromURLs"
        data = {"items": items, "folderId": folder_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def add_item_from_path(
        self,
        path: str,
        name: str,
        website: Optional[str] = None,
        tags: Optional[List[str]] = None,
        annotation: Optional[str] = None,
        folder_id: Optional[str] = None
    ) -> dict:
        """
        POST Add a local file to Eagle App. If you intend to add multiple items in a row, 
        we suggest you use /api/item/addFromPaths.

        Parameters:
        path (str): Required, the path of the local file.
        name (str): Required, the name of the image to be added.
        website (str): The Address of the source of the image.
        annotation (str): The annotation for the image.
        tags (list): Tags for the image.
        folder_id (str): If this parameter is defined, the image will be added to the corresponding folder.

        Returns:
        dict: The response from the server.
        """
        url = f"{self.base_url}/api/item/addFromPath"
        data = {
            "path": path,
            "name": name,
            "website": website,
            "tags": tags,
            "annotation": annotation,
            "folderId": folder_id
        }
        response = requests.post(url, json=data)
        return response.json()

    def add_items_from_paths(
        self,
        items: List[Dict[str, Optional[str]]],
        folder_id: Optional[str] = None
    ) -> dict:
        """
        POST Add multiple local files to Eagle App.

        Parameters:
        items (list): The array object made up of multiple items. Each item should have the following structure:
            - path (str): Required, the path of the local files.
            - name (str): Required, the name of images to be added.
            - website (str): The Address of the source of the images.
            - annotation (str): The annotation for the images.
            - tags (list): Tags for the images.
        folder_id (str): If this parameter is defined, the image will be added to the corresponding folder.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/addFromPaths"
        data = {"items": items, "folderId": folder_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def add_bookmark(
        self,
        url: str,
        name: str,
        tags: Optional[List[str]],
        base64_data: str
    ) -> dict:
        """
        POST Save the link in the URL form to Eagle App.

        Parameters:
        url (str): Required, the link of the image to be saved. Supports http, https, base64.
        name (str): Required, the name of the image to be added.
        base64_data (str): The thumbnail of the bookmark. Must be in base64 format.
        tags (list): Tags for the image.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/addBookmark"
        data = {
            "url": url,
            "name": name,
            "tags": tags,
            "base64": base64_data
        }
        response = requests.post(api_url, json=data)
        return response.json()

    def get_item_info(self, item_id: str) -> dict:
        """
        GET Get Properties of the specified file, including the file name, tags, categorizations, folders, dimensions, etc.

        Parameters:
        item_id (str): ID of the file.

        Returns:
        dict: The response from the server.
        """
        url = f"{self.base_url}/api/item/info?id={item_id}"
        response = requests.get(url)
        return response.json()

    def get_item_thumbnail(self, item_id: str) -> dict:
        """
        GET Get the path of the thumbnail of the file specified. If you would like to get a batch of thumbnail paths, 
        the combination of Library path + Object ID is recommended.

        Parameters:
        item_id (str): ID of the file.

        Returns:
        dict: The response from the server.
        """
        url = f"{self.base_url}/api/item/thumbnail?id={item_id}"
        response = requests.get(url)
        return response.json()

    def list_items(
        self,
        order_by: str,
        limit: int,
        ext: str,
        name: str,
        folders: List[str],
        tags: List[str]
    ) -> dict:
        """
        GET Get items that match the filter condition.

        Parameters:
        order_by (str): The sorting order. Options: CREATEDATE, FILESIZE, NAME, RESOLUTION. Add a minus sign for descending order: -FILESIZE.
        limit (int): The number of items to be displayed. The default number is 200.
        ext (str): Filter by the extension type, e.g., jpg, png.
        name (str): Filter by the keyword.
        folders (list): Filter by folders. Use ',' to divide folder IDs. E.g., KAY6NTU6UYI5Q,KBJ8Z60O88VMG.
        tags (list): Filter by tags. Use ',' to divide different tags. E.g., Design, Poster.

        Returns:
        dict: The response from the server.
        """
        url = f"{self.base_url}/api/item/list"
        params = {
            "orderBy": order_by,
            "limit": limit,
            "ext": ext,
            "name": name,
            "folders": folders,
            "tags": ",".join(tags)
        }
        response = requests.get(url, params=params)
        return response.json()

    def move_items_to_trash(self, item_ids: List[str]) -> dict:
        """
        POST Move items to trash.

        Parameters:
        item_ids (list): Required, list of item IDs to be moved to trash.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/moveToTrash"
        data = {"itemIds": item_ids}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_palette(self, item_id: str) -> dict:
        """
        POST Re-analysis the color of the file. When changes to the original file were made, 
        you can call this function to refresh the Color Analysis.

        Parameters:
        item_id (str): The item's ID.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/refreshPalette"
        data = {"id": item_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_thumbnail(self, item_id: str) -> dict:
        """
        POST Re-generate the thumbnail of the file used to display in the List. 
        When changes to the original file were made, you can call this function to re-generate the thumbnail, 
        the color analysis will also be made.

        Parameters:
        item_id (str): The item's ID.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/refreshThumbnail"
        data = {"id": item_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def update_item(
        self,
        item_id: str,
        tags: Optional[List[str]] = None,
        annotation: Optional[str] = None,
        url: Optional[str] = None,
        star: Optional[int] = None
    ) -> dict:
        """
        POST Modify data of specified fields of the item.

        Tasks that can be done with this function:
        - Text output from external OCR Tools can be added as tags, annotations to the image, and serve as search conditions for later use.
        - The analysis result of the image generated by external Object Detection Tools can be added in the form of tags, and serve as a search condition.

        Parameters:
        item_id (str): Required, the ID of the item to be modified.
        tags (list): Optional, tags.
        annotation (str): Optional, annotations.
        url (str): Optional, the source URL.
        star (int): Optional, ratings.

        Returns:
        dict: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/update"
        data = {
            "id": item_id,
            "tags": tags,
            "annotation": annotation,
            "url": url,
            "star": star
        }
        response = requests.post(api_url, json=data)
        return response.json()
