# Dependencies
import json
import requests as req

# Save config information
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "London"

# Build query URL
query_url = url + "appid=" + api_key + "&q=" + city

# Get weather data
weather_response = req.get(query_url)
weather_json = weather_response.json()

def get_schema(record):
	schema = dict()
	for key, value in record.items():
		if isinstance(value, dict):
			schema[key] = get_schema(value)
		elif isinstance(value, list):
			schema[key] = [get_schema(value[0])]
		else:
			schema[key] = str(type(value))
	return schema

print()
print("Response schema: ")
print(json.dumps(get_schema(weather_json), indent=4))



# Get the temperature from the response
print("The weather API responded with: \n" + json.dumps(weather_json, indent=4) + ".")
