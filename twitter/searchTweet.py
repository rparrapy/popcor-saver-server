import tweepy
import pandas
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "3673450215-goBPtouzfB2MlC7tayO96EjLzxOCNqlFpbhVPSr"
access_token_secret = "yazMGM2wrQDdObpwNNAhiJlqIVfT0U9dyr9OSGbcucJQS"
consumer_key = "cV1w6r6z6w9eEfpwDt1xiWFQg"
consumer_secret = "2wGLylL0GiFeUwUbw9gBfvblLlYNRfz78aQbXTeHuSrUOJxPPD"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
results = []

#Get the first 5000 items based on the search query
for tweet in tweepy.Cursor(api.search, q='Jupiter Ascending').items(300):
    print tweet
    results.append(tweet)
    #break

#tweet = results[0] #Get the first tweet in the result
#
# # Analyze the data in one tweet to see what we require
# for param in dir(tweet):
# # #The key names beginning with an '_' are hidden ones and usually not required, so we'll skip them
#      if not param.startswith("_"):
#          print "%s : %s\n" % (param, eval('tweet.'+param))

# Verify the number of items returned
#print len(results)

# Create a function to convert a given list of tweets into a Pandas DataFrame.
# The DataFrame will consist of only the values, which I think might be useful for analysis...


def toDataFrame(tweets):

    DataSet = pandas.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]


    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]

    return DataSet

#Pass the tweets list to the above function to create a DataFrame
DataSet = toDataFrame(results)
DataSet = DataSet[DataSet.tweetText.notnull()]
print len(DataSet)
