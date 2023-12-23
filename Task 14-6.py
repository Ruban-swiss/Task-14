import requests

def display_countries_with_euro():
    api_url = "https://restcountries.com/v3.1/all"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            countries = response.json()

            # Display countries with EURO as currency
            for country in countries:
                country_name = country['name']['common']

                # Check if the country has currencies information
                if 'currencies' in country:
                    currencies = country['currencies']
                    for currency_code, currency_info in currencies.items():
                        if 'EURO' in currency_info.get('name', '').upper():
                            # Display country, currency, and symbol information
                            print(f"Country: {country_name}")
                            print(f"Currency: {currency_info.get('name', '')}")
                            print(f"Currency Symbol: {currency_info.get('symbol', '')}")
                            print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the method to display countries with EURO as currency
display_countries_with_euro()
