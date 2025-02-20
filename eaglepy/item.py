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

    def get_item_info(self, item_id):
        url = f"{self.base_url}/api/item/info?id={item_id}"
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
