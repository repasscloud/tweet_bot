import os
import tweepy
import asyncio

API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

def main(tweet_text):
    client = tweepy.Client(consumer_key=API_KEY,
                           consumer_secret=API_SECRET,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_SECRET)
    response = client.create_tweet(text=tweet_text)

async def wait_x_minutes(minutes):
    seconds = minutes * 60
    await asyncio.sleep(seconds)

async def wait_2x_minutes(minutes):
    seconds = (minutes * 60) * 2
    await asyncio.sleep(seconds)
