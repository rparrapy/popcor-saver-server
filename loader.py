#!/usr/bin/env python
from elasticsearch import Elasticsearch
import csv

__author__ = 'rparra'
es = Elasticsearch()


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
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            elem = func(row) if func else row
            result.append(elem)
    return result
