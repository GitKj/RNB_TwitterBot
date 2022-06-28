import tweepy
import os

def get_Twitter_Client():
    return tweepy.Client(
        consumer_key=os.getenv("twitter_api_key"), consumer_secret=os.getenv("twitter_secret_key"),
        access_token=os.getenv("twitter_access_token"), access_token_secret=os.getenv("twitter_access_token_secret")
        )
