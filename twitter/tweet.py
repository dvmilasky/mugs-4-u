from tweepy import *
import logging
import os

client = Client(bearer_token=os.getenv("TWITTER_BEARER"))

user = client.get_user(username="dmilasky")


id = user.data.id

tweets = client.get_users_tweets(id=id)

print(tweets)