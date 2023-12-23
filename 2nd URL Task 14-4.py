import requests

def get_breweries_with_websites_by_state(state):
    api_url = f"https://api.openbrewerydb.org/breweries?by_state={state}"

    try:
        # Fetch data from the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            breweries = response.json()

            # Filter breweries with websites
            breweries_with_websites = [brewery for brewery in breweries if 'website_url' in brewery and brewery['website_url']]

            # Display the count of breweries with websites
            print(f"Number of breweries with websites in {state}: {len(breweries_with_websites)}")
            
            # List the breweries with websites
            if breweries_with_websites:
                print("Breweries with Websites:")
                for brewery in breweries_with_websites:
                    print(f"- {brewery['name']}: {brewery['website_url']}")
                print("----------------------")

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get the count and list of breweries with websites in each state
get_breweries_with_websites_by_state("Alaska")
get_breweries_with_websites_by_state("Maine")
get_breweries_with_websites_by_state("New York")
