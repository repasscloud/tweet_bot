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


def main_with_media(tweet_text, media_path):
    auth = tweepy.OAuth1UserHandler(
       API_KEY,
       API_SECRET,
       ACCESS_TOKEN,
       ACCESS_SECRET
    )

    api = tweepy.API(auth)

    media = api.media_upload(filename=media_path)
    print("MEDIA: ", media)

    client = tweepy.Client(consumer_key=API_KEY,
                           consumer_secret=API_SECRET,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_SECRET)
    
    tweet = client.create_tweet(text=tweet_text,media_ids=[media.media_id_string])

    print("TWEET: ", tweet)
