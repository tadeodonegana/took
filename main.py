from text_to_tweets import txt_to_list_of_tweets, make_sentence_available_for_tweet
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
TIME_DELAY = 1800

# Create the tweepy client
client = tweepy.Client(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_TOKEN_SECRET)

# Start tweet id
original_tweet_id = '1529596970410684416'

book_sentences = txt_to_list_of_tweets('books/the-last-question-asimov.txt')
# Tweets the book, one line every TIME_DELAY seconds
for sentence in book_sentences:
    # Check if the sentence has more than 280 caracters, that's a tweet character limit
    if(len(sentence) >= 280):
        long_sentences = make_sentence_available_for_tweet(sentence)
        # If the the current sentence has more than 280 chars we split that sentence and tweet it
        for long_sentence in long_sentences:
            client.create_tweet(text = long_sentence, in_reply_to_tweet_id = original_tweet_id)
            time.sleep(TIME_DELAY)
    else:
        client.create_tweet(text = sentence, in_reply_to_tweet_id = original_tweet_id)
        time.sleep(TIME_DELAY)
    
    # Get the last tweet (the one created upside)
    tweets = client.get_users_tweets(id=USER_ID, tweet_fields=['context_annotations','created_at','geo'], user_auth=True)

    # Get the id of the last tweet to continue the thread
    original_tweet_id =  tweets.data[0].id