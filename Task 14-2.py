import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.Error as errh:
            print ("Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error :", errc)

url = 'https://restcountries.com/v3.1/all'
country_data = CountryData(url)

# Now you can access the data using the 'country_data' object
print(country_data.data)
