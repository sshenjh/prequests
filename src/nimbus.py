from base import BaseAPI

class AnotherAPI(BaseAPI):
    def __init__(self):
        super().__init__("https://anotherapi.com/api")

    def fetch_another_data(self):
        param_names = ['paramA', 'paramB', 'paramC']
        params = self.get_user_input(param_names)
        return self.fetch_data("another-endpoint", **params)

    def fetch_yet_another_data(self):
        param_names = ['paramX', 'paramY', 'paramZ']
        params = self.get_user_input(param_names)
        return self.fetch_data("yet-another-endpoint", **params)

    def fetch_some_other_data(self):
        param_names = ['param1', 'param2', 'param3']
        params = self.get_user_input(param_names)
        return self.fetch_data("some-other-endpoint", **params)

        

# Example usage:
another_api = AnotherAPI()

# Fetch data with user-provided parameters for the specific endpoint
response = another_api.fetch_another_data()
print(response.url)  # Check the URL to see the parameters
print(response.json())  # Assuming the response is in JSON format
