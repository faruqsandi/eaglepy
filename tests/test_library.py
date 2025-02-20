import unittest
from unittest.mock import patch, Mock
from eaglepy.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(base_url="http://localhost:41595")

    @patch('requests.get')
    def test_get_library_info(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"info": "test"}
        mock_get.return_value = mock_response

        response = self.library.get_library_info()
        self.assertEqual(response, {"info": "test"})
        mock_get.assert_called_once_with("http://localhost:41595/api/library/info")

    @patch('requests.post')
    def test_switch_library(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        response = self.library.switch_library("path/to/library")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once_with("http://localhost:41595/api/library/switch",
                                          json={"libraryPath": "path/to/library"})

    @patch('requests.get')
    def test_get_library_history(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"history": ["lib1", "lib2"]}
        mock_get.return_value = mock_response

        response = self.library.get_library_history()
        self.assertEqual(response, {"history": ["lib1", "lib2"]})
        mock_get.assert_called_once_with("http://localhost:41595/api/library/history")

    def test_get_library_icon(self):
        library_path = "path/to/library"
        expected_url = f"http://localhost:41595/api/library/icon?libraryPath={library_path}"
        response = self.library.get_library_icon(library_path)
        self.assertEqual(response, expected_url)


if __name__ == '__main__':
    unittest.main()
