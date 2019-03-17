import tweepy
import random

CONSUMER_KEY="xxx"
CONSUMER_SECRET="xxx"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN='xxx'
ACCESS_SECRET='xxx'
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api=tweepy.API(auth)

STATUS_DATA=["abc","bcd",
             "cde","def"]
api.update_status(random.choice(STATUS_DATA))
