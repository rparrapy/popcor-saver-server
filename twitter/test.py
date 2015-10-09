

import tweepy
import sys
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "3673450215-goBPtouzfB2MlC7tayO96EjLzxOCNqlFpbhVPSr"
access_token_secret = "yazMGM2wrQDdObpwNNAhiJlqIVfT0U9dyr9OSGbcucJQS"
consumer_key = "cV1w6r6z6w9eEfpwDt1xiWFQg"
consumer_secret = "2wGLylL0GiFeUwUbw9gBfvblLlYNRfz78aQbXTeHuSrUOJxPPD"

#Write output to a File
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Files/Tweets.txt", "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

#Set the output to be on terminal and on the file
sys.stdout = Logger()

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['maze runner', 'movie', 'action'])
