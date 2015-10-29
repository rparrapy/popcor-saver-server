__author__ = 's150834'
#Imports
from elasticsearch import Elasticsearch
from pymongo import MongoClient
import csv
import re
from tweetHarvest import tweepyHandler
from polarity_tweet import blobPolarity

#Variables
es = Elasticsearch()
gather = tweepyHandler()
polarity = blobPolarity()
base_path = '../../static/csv/'

#Functions

def string_without_spaces(str):#returns a string with beginning and ending white spaces deleted and adds word movie at the end
    return str.lstrip().rstrip() + ' movie'
def get_tweets(movie_name, number_tweets=40):#gets at most 40 tweets by default from a topic and returns a list [[{"text":"movie tweet","polarity":"0.9", "naive":"pos"}, , ]
    result = []
    my_tweets = gather.getTweets(string_without_spaces(movie_name),number_tweets)
    my_tweets = gather.encode_list_utf8(my_tweets)
    #gather.printArray(my_tweets)#print with utf-8
    for tweet in my_tweets:
        try:
            element = {"text": ''+tweet,"polarity": str(polarity.get_polarity(tweet)), "naive":"pos"}
            result.append(element)
        except:
            pass
    #print len(result)
    #print 'Printing results list'
    # for r in result:
    #     print r
    return result
def load_elasticsearch():
    links = _process_links()
    movies = _read_csv(base_path + 'movies.csv', lambda m: _process_movie(m, links))
    success = 0
    error = 0
    random_list = []
    for movie in movies:
        movie_title_with_year = movie['title']
        movie_title_without_year = movie_title_with_year.split('(')
        #print movie#movie_title[0], movie['movieId']
        print 'Getting movie: ' + movie_title_without_year[0] + ' tweets...'
        es.index(index='movie_tweets', doc_type='movie', id=movie['movieId'], body={
            'title': movie_title_without_year[0],
            'movieId' : movie['movieId'],
            'tweets' : get_tweets(string_without_spaces(movie_title_without_year[0]),50)
        })
        #break
        # res = es.index(index='popcorn-saver', doc_type='movie', id=movie['movieId'], body=movie)
        # if res:
        #     success += 1
        # else:
        #     error += 1

    #print 'Indexing complete: %s succesful operations, %s errors' % (success, error)
    return {'success': success, 'error': error}
def _process_links():
    links = {}

    def process_link(l):
        return {l['movieId']: {'imdbId': l['imdbId'], 'tmdbId': l['tmdbId']}}

    link_list = _read_csv(base_path + 'links.csv', process_link)

    for l in link_list:
        links.update(l)
    return links
def _process_movie(m, links):
    m.update(links[m['movieId']])
    m['genres'] = m['genres'].split('|')
    year_regex = re.search(r"(\([0-9]+\))", m['title'])
    if year_regex is not None:
        m['year'] = int(year_regex.groups()[0][1:-1])
    return m
def _read_csv(path, func=None, is_reduce=False):
    result = []
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        result = None
        if func is None:
            result = list(reader)
        elif is_reduce:
            result = func(reader)
        else:
            result = map(func, reader)
    return result

#main
if __name__ == '__main__':
    load_elasticsearch()
    #get_tweets('Jupiter Ascending',50)


