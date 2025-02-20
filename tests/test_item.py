import unittest
from unittest.mock import patch, Mock
from eaglepy.item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item(base_url="http://localhost:41595")

    @patch('requests.post')
    def test_add_item_from_url(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.add_item_from_url("http://example.com/image.jpg", "image")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/addFromURL",
            json={"url": "http://example.com/image.jpg", "name": "image",
                  "website": None, "tags": None, "modificationTime": None, "headers": None}
        )

    @patch('requests.post')
    def test_add_items_from_urls(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        items = [{"url": "http://example.com/image1.jpg", "name": "image1"}]
        response = self.item.add_items_from_urls(items)
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/addFromURLs",
            json={"items": items, "folderId": None}
        )

    @patch('requests.post')
    def test_add_item_from_path(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.add_item_from_path("path/to/image.jpg", "image")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/addFromPath",
            json={"path": "path/to/image.jpg", "name": "image", "website": None,
                  "tags": None, "annotation": None, "folderId": None}
        )

    @patch('requests.post')
    def test_add_items_from_paths(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        items = [{"path": "path/to/image1.jpg", "name": "image1"}]
        response = self.item.add_items_from_paths(items)
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/addFromPaths",
            json={"items": items, "folderId": None}
        )

    @patch('requests.post')
    def test_add_bookmark(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.add_bookmark("http://example.com", "bookmark", None, "base64data")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/addBookmark",
            json={"url": "http://example.com", "name": "bookmark", "tags": None, "base64": "base64data"}
        )

    @patch('requests.get')
    def test_get_item_info(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"info": "test"}
        mock_get.return_value = mock_response

        response = self.item.get_item_info("item_id")
        self.assertEqual(response, {"info": "test"})
        mock_get.assert_called_once_with("http://localhost:41595/api/item/info?id=item_id")

    @patch('requests.get')
    def test_get_item_thumbnail(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"thumbnail": "path/to/thumbnail"}
        mock_get.return_value = mock_response

        response = self.item.get_item_thumbnail("item_id")
        self.assertEqual(response, {"thumbnail": "path/to/thumbnail"})
        mock_get.assert_called_once_with("http://localhost:41595/api/item/thumbnail?id=item_id")

    @patch('requests.get')
    def test_list_items(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"items": []}
        mock_get.return_value = mock_response

        response = self.item.list_items("CREATEDATE", 10, "jpg", "name", ["folder1"], ["tag1"])
        self.assertEqual(response, {"items": []})
        mock_get.assert_called_once_with(
            "http://localhost:41595/api/item/list",
            params={"orderBy": "CREATEDATE", "limit": 10, "ext": "jpg",
                    "name": "name", "folders": ["folder1"], "tags": "tag1"}
        )

    @patch('requests.post')
    def test_move_items_to_trash(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.move_items_to_trash(["item1", "item2"])
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/moveToTrash",
            json={"itemIds": ["item1", "item2"]}
        )

    @patch('requests.post')
    def test_refresh_palette(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.refresh_palette("item_id")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/refreshPalette",
            json={"id": "item_id"}
        )

    @patch('requests.post')
    def test_refresh_thumbnail(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.refresh_thumbnail("item_id")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/refreshThumbnail",
            json={"id": "item_id"}
        )

    @patch('requests.post')
    def test_update_item(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.item.update_item("item_id", tags=["tag1"], annotation="note", url="http://example.com", star=5)
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/item/update",
            json={"id": "item_id", "tags": ["tag1"], "annotation": "note", "url": "http://example.com", "star": 5}
        )


if __name__ == '__main__':
    unittest.main()
