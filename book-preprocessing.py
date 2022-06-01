import nltk

# Comment line 5 if you're running the code not for the first time.
# More info about nltk.download() in https://www.nltk.org/api/nltk.html?highlight=nltk%20download#module-nltk.downloader
nltk.download('punkt')

# Converts a .txt to a list of sentences to tweet
def txt_to_list_of_sentences(txt_name):
    with open(txt_name, 'r') as file:
        data = file.read().replace('\n', ' ')
    return nltk.tokenize.sent_tokenize(data)

# Takes a sentence and replaces , for . to tokenize it and be able to tweet it. It's used in case the sentence have more than 280 chars.
def make_sentence_available_for_tweet(sentence):
    sentence = sentence.replace(",", ".")
    return nltk.tokenize.sent_tokenize(sentence)

# Generates a txt file within each line is a tweet ready to be sent
def tweetify_book(txt_name):
    list_of_sentences = txt_to_list_of_sentences('books/'+txt_name)
    
    with open('tweetify-books/tweetify-'+txt_name, 'w') as file:
        for sentence in list_of_sentences:
            if(len(sentence) >= 280):
                long_sentences = make_sentence_available_for_tweet(sentence)
                for long_sentence in long_sentences:
                    file.write(long_sentence+'\n')
            else:
                file.write(sentence+'\n')