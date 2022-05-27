import nltk

# Uncomment line 5 if you're running the code for the first time, then comment it again.
# More info about nltk.download() in https://www.nltk.org/api/nltk.html?highlight=nltk%20download#module-nltk.downloader
nltk.download('punkt')

# Converts a .txt to a list of sentences to tweet
def txt_to_list_of_tweets(txt_name):
    with open(txt_name, 'r') as file:
        data = file.read().replace('\n', ' ')
    return nltk.tokenize.sent_tokenize(data)

# Takes a sentence and replaces , for . to tokenize it and be able to tweet it. It's used in case the sentence have more than 280 chars.
def make_sentence_available_for_tweet(sentence):
    sentence = sentence.replace(",", ".")
    return nltk.tokenize.sent_tokenize(sentence)