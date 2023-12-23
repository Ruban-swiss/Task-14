import requests

def get_breweries_by_state(state):
    api_url = f"https://api.openbrewerydb.org/breweries?by_state={state}"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            breweries = response.json()

            # Display names of breweries
            print(f"Breweries in {state}:")
            for brewery in breweries:
                print(brewery['name'])
            print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# List breweries in Alaska
get_breweries_by_state("Alaska")

# List breweries in Maine
get_breweries_by_state("Maine")

# List breweries in New York
get_breweries_by_state("New York")
