# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

# Twitter API Keys
consumer_key = "je1x951IsN6iW4GGAIwKNZR0d"
consumer_secret = "BY6GjtZOwz8roPEyURqDUFCtxzbvQtaIf47YMMgN6zF4cXz26f"
access_token = "2178614324-aofcZgOC725V0PQW23GKXkYBwJ9V4sSgSRsqRRC"
access_token_secret = "xx92AJ2PHphGutZoP01BJ8TBFodu1HxuZvozaBSZ30Hpg"

# Weather API
api_key = "05b10e9615ebd440d9186991fa573f78"

url = "http://api.openweathermap.org/data/2.5/weather?"
endpoint = "http://api.openweathermap.org/data/2.5/weather"    
units = "metric"

# Create a function that gets the weather in London and Tweets it
def WeatherTweet():
    """Get Weather in London and Tweet it out."""
    # @TODO: Construct a Query URL for the OpenWeatherMap
    city = "London"
    query_url = url + "appid=" + api_key + "&q=" + city
    
    param_dict = {
    	'appid': api_key,
    	'q': city,
    	'units': ['imperial', 'metric']
    }

    # Get weather data
    weather_response = req.get(endpoint, params=param_dict)
    # weather_json = weather_response.json()

    # Get temperature from JSON response
    temperature = weather_json["main"]["temp"]

    # Report temperature
    print("The temperature in London is " + str(temperature) + "!")

    
    # @TODO: Perform the API call to get the weather
If __name__ == '__main__':
    
    
    # @TODO: Twitter credentials

    # @TODO: Tweet the weather

    # @TODO: Print success message

# @TODO: Set timer to run every 1 hour
