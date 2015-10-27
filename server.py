#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS
from loader import load_elasticsearch, load_mongodb, load_quotes
from pymongo import MongoClient

__author__ = 'rparra'
app = Flask(__name__)
app.debug = True
CORS(app)
client = MongoClient()
db = client['popcorn-saver']



@app.route('/')
def index():
    return 'Hello world!'


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    result = None
    if request.method == 'POST':
        dest = request.form.get('dest')
        if dest == 'ES':
            result = jsonify(load_elasticsearch())
        elif dest == 'MONGO':
            result = jsonify(load_mongodb())
    else:
        result = 'Please search directly in ES'
    return result


@app.route('/trends', methods=['GET', 'POST'])
def trends():
    if request.method == 'POST':
        return 'TODO: load trends to elasticsearch'
    else:
        return 'List of trends'


@app.route('/quotes', methods=['POST'])
def quotes(q=None):
    return jsonify(load_quotes())


@app.route('/ratings', methods=['POST', 'DELETE'])
def ratings():
    if request.method == 'POST':
        movie_rating = dict(request.form)
        movie_rating['item_id'] = long(movie_rating['item_id'][0])
        movie_rating['user_id'] = long(movie_rating['user_id'][0])
        movie_rating['created_at'] = long(movie_rating['created_at'][0])
        movie_rating['preference'] = float(movie_rating['preference'][0])

        existing = db['ratings'].find_one({'item_id': movie_rating['item_id'], 'user_id': movie_rating['user_id']})
        if existing:
            existing['preference'] = movie_rating['preference']
            result = db['ratings'].update_one(existing)
        else:
            result = db['ratings'].insert_one(dict(movie_rating))
    else:
        result = db['ratings'].delete_many({'user_id': 0})
    return jsonify({'success': result.acknowledged})


if __name__ == "__main__":
    app.run(debug=True)
