__author__ = 's150834'
#imports
import tweepy, pandas, time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class tweepyHandler():
    #Variables that contains the user credentials to access Twitter API
    access_token = "3673450215-goBPtouzfB2MlC7tayO96EjLzxOCNqlFpbhVPSr"
    access_token_secret = "yazMGM2wrQDdObpwNNAhiJlqIVfT0U9dyr9OSGbcucJQS"
    consumer_key = "cV1w6r6z6w9eEfpwDt1xiWFQg"
    consumer_secret = "2wGLylL0GiFeUwUbw9gBfvblLlYNRfz78aQbXTeHuSrUOJxPPD"
    #Autentication with tweeter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    def getTweets(self,movie_name, num_items=50): #Gives a name and returns an array of tweets
        results = []
        while True:#After n calls to tweet you need to wait 15 minutes to gather more tweets..twitter rule
            try:
                twts = tweepy.Cursor(self.api.search, q=movie_name,lang='en').items(num_items)
                for tweet in twts:
                    results.append(tweet.text)
                break
            except tweepy.TweepError:
                print 'Going to sleep 15 min...'
                time.sleep(60*15)#60 seconds * 15 minutes
                print '15 min ended..Calling again'
                continue
        return results
    def printArray(self,arr):
        for t in arr:
            print t.encode("utf-8")
    def encode_list_utf8(self, arr):
        result = []
        for t in arr:
            result.append(t.encode("utf-8"))
        return result

#main run
if __name__ == "__main__":
    print 'Harvesting tweets:'
    #Run with 1 movie example
    # gather = tweepyHandler()
    # my_tweets = gather.getTweets('Jupiter Ascending movie',50)
    # my_tweets = gather.encode_list_utf8(my_tweets)
    # for t in my_tweets:
    #     print t

    #my_tweets = gather.getTweets('Jurassic Park movie',50)
    #gather.printArray(my_tweets)

