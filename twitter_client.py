import tweepy
import config

def get_Twitter_Client():
    return tweepy.Client(
        consumer_key=config.twitter_api_key, consumer_secret=config.twitter_secret_key,
        access_token=config.twitter_access_token, access_token_secret=config.twitter_access_token_secret
        )
