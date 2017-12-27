# Dependencies
import tweepy
import json
import numpy as np

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "je1x951IsN6iW4GGAIwKNZR0d"
consumer_secret = "BY6GjtZOwz8roPEyURqDUFCtxzbvQtaIf47YMMgN6zF4cXz26f"
access_token = "2178614324-aofcZgOC725V0PQW23GKXkYBwJ9V4sSgSRsqRRC"
access_token_secret = "xx92AJ2PHphGutZoP01BJ8TBFodu1HxuZvozaBSZ30Hpg"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Search Term
target_term = "@CNNbrk"

# @TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
# Add List to hold sentiment
# @TODO: YOUR CODE HERE
compound_list=[]
positive_list=[]
necative_list=[]
neutral_list=[]
# Grab 25 tweets
# @TODO: YOUR CODE HERE
for x in range(25):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_term)

    # Loop through all tweets
    for tweet in public_tweets:

        # Utilize JSON dumps to generate a pretty-printed json
        # print(json.dumps(
        #     tweet, sort_keys=True, indent=4, separators=(',', ': ')))

        # Print Tweets
        print("Tip %s: %s" % (counter, tweet["text"]))

        # Add to Counter
        counter = counter + 1

# Loop through all tweets
# @TODO: YOUR CODE HERE

#  Run Vader Analysis on each tweet
#  @TODO: YOUR CODE HERE
   
#  Add each value to the appropriate array
#  @TODO: YOUR CODE HERE
  
# Store the Average Sentiments
#  @TODO: YOUR CODE HERE

# Print the Sentiments
# @TODO: YOUR CODE HERE

