#!/usr/bin/env python
from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from flask_cors import CORS
from loader import load_elasticsearch, load_mongodb

__author__ = 'rparra'
es = Elasticsearch()
app = Flask(__name__)
app.debug = True
CORS(app)

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


@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':
        return 'TODO: load recommendations to elasticsearch'
    else:
        ratings = request.args.get('ratings')
        return 'List of recommendations'


@app.route('/trends', methods=['GET', 'POST'])
def trends():
    if request.method == 'POST':
        return 'TODO: load trends to elasticsearch'
    else:
        return 'List of trends'


@app.route('/quotes', methods=['POST'])
def quotes():
    return 'TODO: load quotes to elasticsearch'


if __name__ == "__main__":
    app.run(debug=True)
