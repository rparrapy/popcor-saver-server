__author__ = 's150834'


from textblob import TextBlob

class blobPolarity():
    tweet_text = ""
    def get_polarity(self, sentence):
        self.tweet_text = TextBlob(sentence)
        return self.tweet_text.sentiment.polarity

if __name__ == "__main__":
    test = blobPolarity()
    print test.get_polarity("very great")
    print test.get_polarity("I have seen better")
    print test.get_polarity("Some bad film")
