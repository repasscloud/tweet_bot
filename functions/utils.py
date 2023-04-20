from private import config
import tweepy
import asyncio

def main(tweet_text):
    client = tweepy.Client(consumer_key=config.API_KEY,
                           consumer_secret=config.API_SECRET,
                           access_token=config.ACCESS_TOKEN,
                           access_token_secret=config.ACCESS_SECRET)

    response = client.create_tweet(text=tweet_text)

async def wait_x_minutes(minutes):
    seconds = minutes * 60
    await asyncio.sleep(seconds)

async def wait_2x_minutes(minutes):
    seconds = (minutes * 60) * 2
    await asyncio.sleep(seconds)