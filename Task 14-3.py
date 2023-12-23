import requests

class CountryDataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Error as errh:
            print("Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

url = 'https://restcountries.com/v3.1/all'
data_fetcher = CountryDataFetcher(url)

# Fetch data using the method
json_data = data_fetcher.fetch_data()

# Now you can use the 'json_data' variable to access the fetched data
print(json_data)
