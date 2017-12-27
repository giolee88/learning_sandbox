# Dependencies
import tweepy
import json

# Twitter API Keys
consumer_key = "je1x951IsN6iW4GGAIwKNZR0d"
consumer_secret = "BY6GjtZOwz8roPEyURqDUFCtxzbvQtaIf47YMMgN6zF4cXz26f"
access_token = "2178614324-aofcZgOC725V0PQW23GKXkYBwJ9V4sSgSRsqRRC"
access_token_secret = "xx92AJ2PHphGutZoP01BJ8TBFodu1HxuZvozaBSZ30Hpg"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a complimentary status update with a mention to another user
api.update_status("@DaDataBootcamp , Van tolerates my slow-ass typing super well!" ) 