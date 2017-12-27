# Dependencies
import json

import requests as req

# Save config information.
endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
city = "Bujumbura"
units = "metric"

param_dict = {
	'appid': api_key,
	'q': city,
	'units': ['imperial', 'metric']
}

# Get weather data
weather_response = req.get(endpoint, params=param_dict)
weather_json = weather_response.json()

# Get temperature from JSON response
temperature = weather_json["main"]["temp"]

# Report temperature
print("The temperature in Bujumbura is " + str(temperature) + "!")


"""
# SCHEMA STUFF
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
"""