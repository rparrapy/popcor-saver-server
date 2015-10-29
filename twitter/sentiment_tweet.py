#python -m textblob.download_corpora  use in case missing package
import pickle, json
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus import movie_reviews

train_again = False

class objectSaver():
    def save_classifier(self, classifier):
       f = open('naive_training_object.txt', 'wb')
       pickle.dump(classifier, f, -1)
       f.close()
    def load_classifier(self):
       f = open('naive_training_object.txt', 'rb')
       classifier = pickle.load(f)
       f.close()
       return classifier

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg'),
    ('Had a bad ending taste', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

# reviews = [(list(movie_reviews.words(fileid)), category)
#               for category in movie_reviews.categories()
#               for fileid in movie_reviews.fileids(category)]
# new_train, new_test = reviews[0:100], reviews[101:200]
#print(new_train[0])

# with open('line_sentence_merge.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")

# with open('training_set.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")

# with open('testInputFile.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")

# cl = NaiveBayesClassifier(train)
#cl = NaiveBayesClassifier(new_train)


# with open('testInputFile.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")

obj_hand = objectSaver()

if train_again == True:
    # cl = NaiveBayesClassifier(train)
    # obj_hand.save_classifier(cl)
    with open('training_set.json', 'r') as fp:
        cl = NaiveBayesClassifier(fp, format="json")
    obj_hand.save_classifier(cl)
else:
    cl = obj_hand.load_classifier()


#Testing Data section
# print 'Running test data to gather accuracy()...'
# # #print cl.accuracy('testing_set.json', format="json")
# with open('testing_set.json') as data_file:
#     test_data = json.load(data_file)
#
#
# total_entry = len(test_data)
# print 'Testing with ' + str(total_entry)+ ' elements'
# correct_num = 0
# for tst in test_data:
#     correct_value = tst['label']
#     text_from_json = tst['text']
#     value_from_classify = cl.classify(text_from_json)
#     #print correct_value
#     #print value_from_classify
#     if correct_value == value_from_classify:
#         correct_num+=1
#     #break
# print 'Accuracy value: ' + str(correct_num/total_entry)
# print 'End of Accuracy trial'


#Test own values
print(cl.classify("can`t believe i missed out on a day of swimming at nikki`s!")) #neg
print(cl.classify("can't stop smiling after talking to him all day...  ...Why couldn't I have met him months ago?!?")) #pos
print(cl.classify("chillin!!!!")) #pos
# print(cl.classify("plot : two teen couples go to a church party , drink and then drive ."))  # "pos"
# print(cl.classify("Isad for all my friends"))   # "neg"
# print(cl.classify("Worst movie in the world"))   # "neg"
# print(cl.classify("Best movie ever"))   # "pos"
# print(cl.classify("mi bf is cheating on me"))   # "neg"
# print(cl.classify("enjoyable tasks"))   # "pos"










