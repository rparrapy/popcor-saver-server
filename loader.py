#!/usr/bin/env python
from elasticsearch import Elasticsearch
from fuzzywuzzy import fuzz
import csv
import json
import sys

__author__ = 'rparra'
es = Elasticsearch()

reload(sys)  
sys.setdefaultencoding('Cp1252')

def load_movies():
    base_path = 'static/csv/'
    links = {}

    def process_link(l):
        return {l['movieId']: {'imdbId': l['imdbId'], 'tmdbId': l['tmdbId']}}

    link_list = _read_csv(base_path + 'links.csv', process_link)
    for l in link_list:
        links.update(l)

    def process_movie(m):
        m.update(links[m['movieId']])
        m['genres'] = m['genres'].split('|')
        return m

    movies = _read_csv(base_path + 'movies.csv', process_movie)
    success = 0
    error = 0
    for movie in movies:
        res = es.index(index='popcorn-saver', doc_type='movie', id=movie['movieId'], body=movie)
        if res:
            success += 1
        else:
            error += 1
    print 'Indexing complete: %s succesful operations, %s errors' % (success, error)
    return {'success': success, 'error': error}

def _read_csv(path, func=None):
    result = []
    with open(path, 'rU') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            elem = func(row) if func else row
            result.append(elem)
    return result

def load_quotes():
    base_path = 'static/csv/'
    result ={}
    c = 0
    with open(base_path + 'movies.csv', 'rU') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
                title_csv = row[1][0:len(row[1])-6]
                id_csv = row[0]
                quote_list = []
                with open(base_path + 'what.json', 'r') as f:
                    quote_list = json.loads(f.read())
                    for q in quote_list:
                        if len(q['quotes'])>2:
                            ratio = fuzz.ratio( q['title'], title_csv)
                            if ratio > 90:
                                c = c + 1
                                movies=es.get(index='popcorn-saver', doc_type='movie', id=id_csv)
                                movies['quotes']=q['quotes']
                                es.index(index='popcorn-saver', doc_type='movie', id=id_csv, body=movies)
    return {'success': c}


