#!/usr/bin/env python
from elasticsearch import Elasticsearch
import csv

__author__ = 'rparra'
es = Elasticsearch()



def load_elasticsearch():
    links = _process_links()
    movies = _read_csv(base_path + 'movies.csv', lambda m: _process_movie(m, links))
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


def load_mongodb():
    links = _process_links()
    movies = _read_csv(base_path + 'movies.csv', lambda m: _process_movie(m, links))
    movies_result = db['movies'].insert_many(movies)

    def _get_user_list(users, r):
        user_rating = dict((k, r[k]) for k in ('movieId', 'rating', 'timestamp'))
        user_rating['rating'] = float(user_rating['rating'])
        user_rating['timestamp'] = float(user_rating['timestamp'])
        if r['userId'] in users:
            users[r['userId']]['ratings'].append(user_rating)
        else:
            users[r['userId']] = {'userId': r['userId'], 'ratings': [user_rating]}
        return users

    def _process_rating(r):
        result = {}
        result['user_id'] = long(r['userId'])
        result['item_id'] = long(r['movieId'])
        result['preference'] = float(r['rating'])
        result['created_at'] = long(r['timestamp'])
        return result

    users = _read_csv(base_path + 'ratings.csv', lambda r: reduce(_get_user_list, r, {}), is_reduce=True)
    users_result = db['users'].insert_many(users.values())

    ratings = _read_csv(base_path + 'ratings.csv', lambda r: _process_rating(r))
    ratings_result = db['ratings'].insert_many(ratings)
    return {
        'movies': len(movies_result.inserted_ids),
        'users': len(users_result.inserted_ids),
        'ratings': len(ratings_result.inserted_ids)
    }


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
    with open(path, 'rU') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        result = None
        if func is None:
            result = list(reader)
        elif is_reduce:
            result = func(reader)
        else:
            result = map(func, reader)
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


