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

hashtag = f"#{adjetive[:1]}{animal[:1]}{activity[:1]}{club[:1]}"

message = f"{adjetive} {animal} {activity} {club}\n#NFT {hashtag}"

client.create_tweet(text=message)
