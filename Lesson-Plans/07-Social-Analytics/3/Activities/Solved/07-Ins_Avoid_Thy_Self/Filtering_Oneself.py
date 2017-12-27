# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "je1x951IsN6iW4GGAIwKNZR0d"
consumer_secret = "BY6GjtZOwz8roPEyURqDUFCtxzbvQtaIf47YMMgN6zF4cXz26f"
access_token = "2178614324-aofcZgOC725V0PQW23GKXkYBwJ9V4sSgSRsqRRC"
access_token_secret = "xx92AJ2PHphGutZoP01BJ8TBFodu1HxuZvozaBSZ30Hpg"

# Target Term
target_term = "@SouthwestAir"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Search for all tweets
public_tweets = api.search(target_term, count=5, result_type="recent")

# Loop through all public_tweets
for tweet in public_tweets["statuses"]:

    # Get ID and Author of most recent tweet directed to me
    tweet_id = tweet["id"]
    tweet_author = tweet["user"]["screen_name"]
    tweet_text = tweet["text"]

    # Print Tweet Text and Tweet Author
    print(tweet_text)
    print(tweet_author)
