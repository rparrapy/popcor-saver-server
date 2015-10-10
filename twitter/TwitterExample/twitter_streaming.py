import time
from mongoHandler import mongoHandler
# On apps.twitter we are using PopcornSaver app keys
# Import the necessary methods from tweepy library

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "3673450215-goBPtouzfB2MlC7tayO96EjLzxOCNqlFpbhVPSr"
access_token_secret = "yazMGM2wrQDdObpwNNAhiJlqIVfT0U9dyr9OSGbcucJQS"
consumer_key = "cV1w6r6z6w9eEfpwDt1xiWFQg"
consumer_secret = "2wGLylL0GiFeUwUbw9gBfvblLlYNRfz78aQbXTeHuSrUOJxPPD"
start_time = time.time()  # grabs the system time
#keyword_list = ['best action movie', 'action movie', 'must see movie', 'great movie', 'new movie']  # track list
keyword_list = ['avengers']
file_name = None

class Listener(StreamListener):
    def __init__(self, time_limit=60):
        start_time = time.time()
        self.time = start_time
        self.limit = time_limit
    def on_data(self, data):
        while (time.time() - self.time) < self.limit:
            try:
                saveFile = open('raw_tweets.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass
        exit()

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # movie_titles = mongoHandler()
    # movie_titles_array = movie_titles.connect()
    # for doc in movie_titles_array:
    #     #title = movie_titles.splitTitle(doc['title'])
    #     #print title
    #     title="avengers"
    #     title2 = [title]
    #     auth = OAuthHandler(consumer_key, consumer_secret)  # OAuth object
    #     auth.set_access_token(access_token, access_token_secret)
    #     twitterStream = Stream(auth, Listener(start_time, time_limit=20))  # initialize Stream object with a time out limit
    #     twitterStream.filter(track=title2, languages=['en'])  # call the filter method to run the Stream Object
    #     break


    auth = OAuthHandler(consumer_key, consumer_secret)  # OAuth object
    auth.set_access_token(access_token, access_token_secret)
    twitterStream = Stream(auth, Listener(time_limit=10))  # initialize Stream object with a time out limit
    twitterStream.filter(track=keyword_list, languages=['en'])  # call the filter method to run the Stream Object
