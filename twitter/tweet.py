from tweepy import *
import logging
import os

client = Client(bearer_token=os.environ['TWITTER_BEARER'])

me = client.get_user(username="dmilasky")


print(me)