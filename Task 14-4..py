import requests

def display_country_info():
    api_url = "https://restcountries.com/v3.1/all"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            countries = response.json()

            # Display information for each country
            for country in countries:
                country_name = country['name']['common']

                # Check if the country has currencies information
                if 'currencies' in country:
                    currencies = country['currencies']
                    for currency_code, currency_info in currencies.items():
                        currency_name = currency_info.get('name', '')
                        currency_symbol = currency_info.get('symbol', '')

                        # Display country, currency, and symbol information
                        print(f"Country: {country_name}")
                        print(f"Currency: {currency_name}")
                        print(f"Currency Symbol: {currency_symbol}")
                        print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the method to display country information
display_country_info()
