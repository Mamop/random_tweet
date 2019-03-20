import tweepy
import random
import os

def puttweet():
  CONSUMER_KEY=os.environ.get("Consumer_key")
  CONSUMER_SECRET=os.environ.get("Consumer_secret")
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  ACCESS_TOKEN=os.environ.get("Access_token_key")
  ACCESS_SECRET=os.environ.get("Access_token_secret")
  auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

  api=tweepy.API(auth)

  abc=os.environ.get("text1")
  bcd=os.environ.get("text2")
  cde=os.environ.get("text3")
  de=os.environ.get("text4")

  STATUS_DATA=[abc,bcd,
              cde,de]
  api.update_status(random.choice(STATUS_DATA))
