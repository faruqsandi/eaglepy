import requests
from typing import Optional, List, Dict, Union


class Item:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def add_item_from_url(
        self,
        url: str,
        name: str,
        website: Optional[str] = None,
        tags: Optional[List[str]] = None,
        modification_time: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST add an image from a URL to Eagle App.

        Parameters:
            url (str): The URL of the image to be added. Supports http, https, base64.
            name (str): The name of the image to be added.
            website (Optional[str]): The address of the source of the image.
            tags (Optional[List[str]]): Tags for the image.
            modification_time (Optional[int]): The creation date of the image.
            headers (Optional[Dict[str, str]]): Customize the HTTP headers properties.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
        items: List[Dict[str, Optional[Union[str, List[str], int]]]],
        folder_id: Optional[str] = None
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST add multiple images from URLs to Eagle App.

        Parameters:
            items (List[Dict[str, Optional[Union[str, List[str], int]]]]): The array object made up of multiple items.
            folder_id (Optional[str]): If defined, images will be added to the corresponding folder.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST add a local file to Eagle App.

        Parameters:
            path (str): The path of the local file.
            name (str): The name of the image to be added.
            website (Optional[str]): The address of the source of the image.
            annotation (Optional[str]): The annotation for the image.
            tags (Optional[List[str]]): Tags for the image.
            folder_id (Optional[str]): If defined, the image will be added to the corresponding folder.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
        items: List[Dict[str, Optional[Union[str, List[str]]]]],
        folder_id: Optional[str] = None
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST add multiple local files to Eagle App.

        Parameters:
            items (List[Dict[str, Optional[Union[str, List[str]]]]]): The array object made up of multiple items.
            folder_id (Optional[str]): If defined, the image will be added to the corresponding folder.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST save the link in the URL form to Eagle App.

        Parameters:
            url (str): The link of the image to be saved. Supports http, https, base64.
            name (str): The name of the image to be added.
            base64_data (str): The thumbnail of the bookmark in base64 format.
            tags (Optional[List[str]]): Tags for the image.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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

    def get_item_info(self, item_id: str) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        GET properties of the specified file, including the file name, tags, categorizations, folders, dimensions, etc.

        Parameters:
            item_id (str): ID of the file.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
        """
        url = f"{self.base_url}/api/item/info?id={item_id}"
        response = requests.get(url)
        return response.json()

    def get_item_thumbnail(self, item_id: str) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        GET the path of the thumbnail of the specified file.

        Parameters:
            item_id (str): ID of the file.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        GET items that match the filter condition.

        Parameters:
            order_by (str): The sorting order. Options: CREATEDATE, FILESIZE, NAME, RESOLUTION.
            limit (int): The number of items to be displayed. Default is 200.
            ext (str): Filter by the extension type, e.g., jpg, png.
            name (str): Filter by the keyword.
            folders (List[str]): Filter by folders. Use ',' to divide folder IDs.
            tags (List[str]): Filter by tags. Use ',' to divide different tags.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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

    def move_items_to_trash(self, item_ids: List[str]) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST move items to trash.

        Parameters:
            item_ids (List[str]): List of item IDs to be moved to trash.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/moveToTrash"
        data = {"itemIds": item_ids}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_palette(self, item_id: str) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST re-analyze the color of the file.

        Parameters:
            item_id (str): The item's ID.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
        """
        api_url = f"{self.base_url}/api/item/refreshPalette"
        data = {"id": item_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_thumbnail(self, item_id: str) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST re-generate the thumbnail of the file.

        Parameters:
            item_id (str): The item's ID.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
    ) -> Dict[str, Union[str, int, List[str], Dict[str, str]]]:
        """
        POST modify data of specified fields of the item.

        Parameters:
            item_id (str): The ID of the item to be modified.
            tags (Optional[List[str]]): Tags.
            annotation (Optional[str]): Annotations.
            url (Optional[str]): The source URL.
            star (Optional[int]): Ratings.

        Returns:
            Dict[str, Union[str, int, List[str], Dict[str, str]]]: The response from the server.
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
