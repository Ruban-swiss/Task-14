import requests

def get_brewery_count_by_state(state):
    api_url = f"https://api.openbrewerydb.org/breweries?by_state={state}"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            breweries = response.json()

            # Display the count of breweries
            print(f"Number of breweries in {state}: {len(breweries)}")
            print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get the count of breweries in each state
get_brewery_count_by_state("Alaska")
get_brewery_count_by_state("Maine")
get_brewery_count_by_state("New York")
