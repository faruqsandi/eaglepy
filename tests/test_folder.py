import unittest
from unittest.mock import patch, Mock
from eaglepy.folder import Folder


class TestFolder(unittest.TestCase):
    def setUp(self):
        self.folder = Folder(base_url="http://localhost:41595")

    @patch('requests.post')
    def test_create_folder(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.folder.create_folder("New Folder")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/folder/create",
            json={"folderName": "New Folder", "parent": None}
        )

    @patch('requests.post')
    def test_rename_folder(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.folder.rename_folder("folder_id", "Renamed Folder")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/folder/rename",
            json={"folderId": "folder_id", "newName": "Renamed Folder"}
        )

    @patch('requests.post')
    def test_update_folder(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.folder.update_folder("folder_id", "Updated Folder", "New Description", "blue")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with(
            "http://localhost:41595/api/folder/update",
            json={"folderId": "folder_id", "newName": "Updated Folder",
                  "newDescription": "New Description", "newColor": "blue"}
        )

    @patch('requests.get')
    def test_list_folders(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"folders": []}
        mock_get.return_value = mock_response

        response = self.folder.list_folders()
        self.assertEqual(response, {"folders": []})
        mock_get.assert_called_once_with("http://localhost:41595/api/folder/list")

    @patch('requests.get')
    def test_list_recent_folders(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"recentFolders": []}
        mock_get.return_value = mock_response

        response = self.folder.list_recent_folders()
        self.assertEqual(response, {"recentFolders": []})
        mock_get.assert_called_once_with("http://localhost:41595/api/folder/listRecent")


if __name__ == '__main__':
    unittest.main()
