# main.py
from nimbus import AnotherAPI

def main():
    # # ExampleAPI usage
    # example_api = ExampleAPI()
    # response = example_api.fetch_example_data()
    # print(response.url)  # Check the URL to see the parameters
    # print(response.json())  # Assuming the response is in JSON format

    # AnotherAPI usage
    another_api = AnotherAPI()
    response = another_api.fetch_another_data()
    print(response.url)  # Check the URL to see the parameters
    print(response.json())  # Assuming the response is in JSON format

if __name__ == "__main__":
    main()
