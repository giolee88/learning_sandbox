# Dependencies
import json
import requests

# Google developer API key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# Target city
# Boise, Idaho {"lat": 43.6187102, "lng": -116.2146068}
# New York, NY {"lat": 40.7128, "lng": -74.0059}
target_city = {"lat": 43.6187102, "lng": -116.2146068}

# Build the endpoint URL (Checks all ice cream shops)
radar_endpoint = "https://maps.googleapis.com/maps/api/place/radarsearch/json"
radar_params = {
	'location': f'{target_city["lat"]},{target_city["lng"]}',
	'keyword': 'ice cream',
	'type': 'food',
	'radius': 8000,
	'key': gkey
}

# Run a request to endpoint and convert result to json
response = requests.get(radar_endpoint, params=radar_params)
print(response.text)
ice_cream_data = response.json()

# Print the number of ice cream shops
print(json.dumps(ice_cream_data, indent=4))
print(len(ice_cream_data["results"]))
