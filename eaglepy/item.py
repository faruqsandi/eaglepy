import requests


class Item:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_item_from_path(self, path, name, website, tags, annotation, folder_id):
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

    def add_item_from_url(self, url, name, website, tags, modification_time, headers):
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

    def add_items_from_urls(self, items, folder_id):
        api_url = f"{self.base_url}/api/item/addFromURLs"
        data = {"items": items, "folderId": folder_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def add_items_from_paths(self, items, folder_id):
        api_url = f"{self.base_url}/api/item/addFromPaths"
        data = {"items": items, "folderId": folder_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def add_bookmark(self, url, name, tags, base64_data):
        api_url = f"{self.base_url}/api/item/addBookmark"
        data = {
            "url": url,
            "name": name,
            "tags": tags,
            "base64": base64_data
        }
        response = requests.post(api_url, json=data)
        return response.json()

    def get_item_info(self, item_id):
        url = f"{self.base_url}/api/item/info?id={item_id}"
        response = requests.get(url)
        return response.json()

    def get_item_thumbnail(self, item_id):
        url = f"{self.base_url}/api/item/thumbnail?id={item_id}"
        response = requests.get(url)
        return response.json()

    def list_items(self, order_by, limit, ext, name, folders, tags):
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

    def move_items_to_trash(self, item_ids):
        api_url = f"{self.base_url}/api/item/moveToTrash"
        data = {"itemIds": item_ids}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_palette(self, item_id):
        api_url = f"{self.base_url}/api/item/refreshPalette"
        data = {"id": item_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def refresh_thumbnail(self, item_id):
        api_url = f"{self.base_url}/api/item/refreshThumbnail"
        data = {"id": item_id}
        response = requests.post(api_url, json=data)
        return response.json()

    def update_item(self, item_id, tags, annotation, url, star):
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
