import sys
import datetime
import random
import asyncio

from csv_reader import read_csv_file
from utils import main, main_with_media, wait_2x_minutes, wait_x_minutes

if len(sys.argv) > 2:
    main_with_media(tweet_text=sys.argv[1],media_path=sys.argv[2])
    sys.exit()
elif len(sys.argv) > 1:
    text_to_tweet = sys.argv[1]  # get the first command-line argument as tweet_text
    tweet_text = text_to_tweet
else:
    # read the csv data file and assign value to tweet_text
    csv_data = 'data.csv'
    result = read_csv_file(csv_file_path=csv_data)
    if result is not None and len(result) == 2:
        text_to_tweet, csv_data = result
    else:
        text_to_tweet = result
    tweet_text = text_to_tweet

# run only if there is a value for today
if text_to_tweet is not None:
    if datetime.datetime.now().strftime('%p') == 'AM':
        # do something if it's AM
        print("is is PM")

        # set a random number of minutes
        random_minutes = random.randint(0, 2)
        print(f"Waiting {random_minutes} mins")

        # pause for random minutes
        asyncio.run(wait_x_minutes(random_minutes))

        if __name__ == '__main__':
            main(tweet_text[1])
    else:
        # do something if it's PM
        print("it is AM")

        # set a random number of minutes
        random_minutes = random.randint(0, 2)
        print(f"Waiting {random_minutes} mins")

        # pause for random minutes
        asyncio.run(wait_2x_minutes(random_minutes))

        if __name__ == '__main__':
            main(tweet_text[0])
else:
    print("There is nothing to tweet today")

