import tweepy
import os
import sys

client = tweepy.Client(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)


(_, adjetive, animal, activity, club) = sys.argv
print(sys.argv)
#
# client.create_tweet(text="Hello")