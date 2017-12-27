# Dependencies
import requests

# Google developer API key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# Target city
target_city = "Boise, Idaho"

params_dict = {
	'address': target_city,
	'key': gkey
}
# Build the endpoint URL
target_url = "https://maps.googleapis.com/maps/api/geocode/json"

# Print the assembled URL

# Run a request to endpoint and convert result to json
response = requests.get(target_url, params=params_dict)
print(response.url)
geo_data = response.json()

# Print the json
print(geo_data)
