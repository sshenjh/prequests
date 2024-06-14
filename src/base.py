import requests
import yaml

class BaseAPI:
    def __init__(self, base_url, config_file=None):
        self.base_url = base_url.rstrip('/')
        self.api_key = None
        
        if config_file:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                self.api_key = config['API_KEYS']['secret_key']

    def fetch_data(self, endpoint, path_params=None, query_params=None):
        url = f"{self.base_url}/{endpoint}"
        
        # Replace path parameters in URL
        if path_params:
            for key, value in path_params.items():
                url = url.replace(f"{{{key}}}", str(value))
        
        # Append API key to query parameters if available
        if self.api_key:
            if query_params is None:
                query_params = {}
            query_params['api_key'] = self.api_key
        
        # Make GET request with query parameters
        response = requests.get(url, params=query_params)
        
        # Handle response
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None
