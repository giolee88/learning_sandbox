# Dependencies
import requests
import json

# Google developer API key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# Target city
target_city = ["Arlington, Virginia", "Spokane, WA", "Boise, Idaho"]

for city in target_city:
	# Build the endpoint URL
	target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
	    "?address=%s&key=%s" % (city, gkey)

	# Print the assembled URL
	#print(target_url)

	# Run a request to endpoint and convert result to json
	geo_data = requests.get(target_url).json()

	# Print the json (pretty printed)
	#print(json.dumps(geo_data, indent=4, sort_keys=True))

	# Extract latitude and longitude
	lat = geo_data["results"][0]["geometry"]["location"]["lat"]
	lng = geo_data["results"][0]["geometry"]["location"]["lng"]

	# Print the latitude and longitude
	print("{city}: {lat}, {lng}".format(
		city=city,
		lat=lat,
		lng=lng))
