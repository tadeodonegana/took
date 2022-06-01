from dotenv import load_dotenv
import tweepy
import time
import os

# Load API Credentials from the .env file
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
# User numerical ID
USER_ID = '1526738098654175232'
# Time delay
TIME_DELAY = 60
# Route to the book to tweet
BOOK_TO_TWEET = 'the-last-question-asimov.txt'

# Create the tweepy client
client = tweepy.Client(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_TOKEN_SECRET)

# Start tweet id
original_tweet_id = '1531849599610195970'

# Get the current index (current tweet to send) open the index.txr file. This is a technique to solve restarting errors.
with open('index.txt', 'r') as file:
    current_index = int(file.readline())

# This function writes the current index value on the index.txt file
def update_index(current_index):
    with open('index.txt', 'w') as file:
        file.write(str(current_index))

# Returns last tweet id, to create a thread
def get_last_tweet_id():
    # Get the last tweet (the one created upside)
    tweets = client.get_users_tweets(id=USER_ID, tweet_fields=['context_annotations','created_at','geo'], user_auth=True)

    return tweets.data[0].id

# Tweets the book, one line every TIME_DELAY seconds
with open('tweetify-books/tweetify-' + BOOK_TO_TWEET, 'r') as file:
    tweets = file.readlines()
    while current_index <= len(tweets):
        original_tweet_id = get_last_tweet_id()
        client.create_tweet(text = tweets[current_index], in_reply_to_tweet_id = original_tweet_id)
        print(tweets[current_index])
        current_index= current_index + 1
        update_index(current_index)
        time.sleep(TIME_DELAY)