"""
Example Stream listener for twitter API.

# Create App: apps.twtiter.com
# API Documentation: https://dev.twitter.com/overview/documentation
"""
from __future__ import print_function
import tweepy
import time
import cnfg


class TweetListener(tweepy.StreamListener):

    def on_status(self, tweet):
        print(tweet.text)

    def on_error(self, error_msg):
        print('Error: {}'.format(error_msg))

    def on_timeout(self):
        print('Timed Out.  Might be rate-limited.  Introduce Delay in the process.  ')
        time.sleep(10)


config = cnfg.load(".twitter_config")

auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])


tweet_listener = TweetListener()
tweet_stream = tweepy.Stream(auth = auth, listener=tweet_listener)

tweet_stream.filter(track=['#mlb', "#cubs", 'world series'])
