import requests

def get_brewery_types_by_city(state):
    api_url = f"https://api.openbrewerydb.org/breweries?by_state={state}"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            breweries = response.json()

            # Group breweries by city
            breweries_by_city = {}
            for brewery in breweries:
                city = brewery.get('city')
                brewery_type = brewery.get('brewery_type')

                # Initialize city entry if not present
                if city not in breweries_by_city:
                    breweries_by_city[city] = set()

                # Add brewery type to the city's set
                breweries_by_city[city].add(brewery_type)

            # Display the count of brewery types in each city
            for city, types in breweries_by_city.items():
                print(f"City: {city}")
                print(f"Number of Brewery Types: {len(types)}")
                print("Brewery Types:", ', '.join(types))
                print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get the count of brewery types in each city for the specified states
get_brewery_types_by_city("Alaska")
get_brewery_types_by_city("Maine")
get_brewery_types_by_city("New York")
