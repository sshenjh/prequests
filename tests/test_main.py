import unittest
from unittest.mock import patch, Mock
from base_api import BaseAPI  # Import the class to be tested
import requests

class TestBaseAPI(unittest.TestCase):
    
    @patch.object(requests, 'get')  # Mock requests.get method
    def test_fetch_data(self, mock_get):
        # Mock the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}  # Mock JSON response
        
        # Configure the mock to return the mock response
        mock_get.return_value = mock_response
        
        # Create an instance of BaseAPI
        base_api = BaseAPI("https://example.com/api")
        
        # Call fetch_data method with mock parameters
        endpoint = "example-endpoint"
        params = {'param1': 'value1', 'param2': 'value2'}
        response = base_api.fetch_data(endpoint, **params)
        
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})
        mock_get.assert_called_once_with('https://example.com/api/example-endpoint', params=params)
