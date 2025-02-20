import unittest
from unittest.mock import patch, Mock
from eaglepy.application import Application


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.application = Application(base_url="http://localhost:41595")

    @patch('requests.get')
    def test_get_info(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"info": "test"}
        mock_get.return_value = mock_response

        response = self.application.get_info()
        self.assertEqual(response, {"info": "test"})
        mock_get.assert_called_once_with("http://localhost:41595/api/application/info")


if __name__ == '__main__':
    unittest.main()
