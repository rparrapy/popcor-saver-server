#!/usr/bin/env python
from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from loader import load_movies

__author__ = 'rparra'
es = Elasticsearch()
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/movies', methods=['GET', 'POST'])
def movies(q=None):
    if request.method == 'POST':
        return jsonify(load_movies())
    else:
        return 'Please search directly in ES'


@app.route('/recommendations')
def recommendations(q=None, methods=['GET', 'POST']):
    if request.method == 'POST':
        return 'TODO: load recommendations to elasticsearch'
    else:
        return 'List of recommendations'


@app.route('/trends', methods=['GET', 'POST'])
def trends(q=None):
    if request.method == 'POST':
        return 'TODO: load trends to elasticsearch'
    else:
        return 'List of trends'


@app.route('/quotes')
def quotes(q=None, methods=['POST']):
    return 'TODO: load quotes to elasticsearch'


if __name__ == "__main__":
    app.run(debug=True)
