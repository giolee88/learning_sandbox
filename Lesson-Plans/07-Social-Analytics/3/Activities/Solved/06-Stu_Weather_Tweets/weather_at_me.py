# Dependencies
import numpy as np
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Target Term
my_twitter = "@gwutweetcamp"

# Opening message
print("We're going live, sir!")


# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create Thank You Function
def get_recent_mentions():
    # Search for all tweets
    return api.search(my_twitter, count=100, result_type="recent")

def asking_for_weather(tweet):
    return "what's the weather in " in tweet['text'].lower()

def get_city(tweet_text):
    # Tweet will be in form "@twitterhandle - What's the weather in <x>?"
    # Split text into preamble (part before city) and city
    preamble, city = tweet_text.lower().split(' in ', 1)

    # Remove question mark from end
    return city[:-1]

def get_weather(city):
    # Construct a Query URL for the OpenWeatherMap
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    param_dict = {
        'q': city,
        'units': 'imperial',
        'appid': api_key
    }

    # Perform the API call to get the weather
    weather_response = req.get(endpoint, params=param_dict)
    return weather_response.json()

def tweet_weather(reply_to, weather_data):
    # Respond to tweet
    api.update_status(
        "The weather in {city} is {weather}".format(
            city=weather_data['city']['name'],
            weather=weather_data['list'][0]['weather']['description']),
        in_reply_to_status_id=reply_to)

    # Print success message
    print("Successful response, sir!")


if __name__ == '__main__':
    # Set timer to run every minute
    while(True):
        recent_mentions = get_recent_mentions()
        for tweet in recent_mentions:
            if asking_for_weather(tweet):
                city = get_city(tweet['text'])
                weather = get_weather(city)
                tweet_weather(weather)
        time.sleep(60)
