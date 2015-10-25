# Popcorn Saver Server

Popcorn Saver is a movie recommendation web application developed as a project for 2IMW15: Web Information Retrieval and Data Mining, during the first quartile of the 2015/2016 academic year at TU Eindhoven. It was developed using the [Movielens 100K](http://grouplens.org/datasets/movielens/) dataset.

This code corresponds to the setup and maintenance server, which a exposes a REST API allowing developers to:
* Load movies from the original dataset to a MongoDB instance, used by the recommender component.
* Load movies from the original dataset to an Elasticsearch instance, used to implement boolean and parametric search from the client component.
* Scrape movie quotes from http://www.moviequotedb.com/.
* Get movie related tweets using the Twitter API.

### Requirements
* A running instance of Elasticsearch on its default port. Installation instructions can be found here: https://www.elastic.co/guide/en/elasticsearch/guide/current/_installing_elasticsearch.html
* A running instance of MongoDB on its default port. Installation instructions can be found here: https://docs.mongodb.org/manual/installation/
* The Movielens 100K CSV files, which can be downloaded from: http://grouplens.org/datasets/movielens/
* Python 2.7 and pip

### Installation
1. Clone the project.
```sh
$ git clone https://github.com/rparrapy/popcorn-saver-server.git && cd popcorn-saver-server
```
2. Create a *static/csv* folder and move the Movielens CSV files there.
3. Create and activate a virtualenv (optional but highly recommended).
```sh
$ virtualenv . && source bin/activate
```
4. Install Python dependencies.
```sh
$ pip install -r requirements.txt
```
5. Run the web server.
```sh
$ python server.py
```
The maintenance server should be running on port 5000.

6. Load movies to MongoDB by sending a POST request to /movies with a parameter dest=MONGO with your favorite HTTP client.

7. Load movies to Elasticsearch by sending a POST request to /movies with a parameter dest=ES with your favorite HTTP client.

8. Load ratings to MongoDB by sending a POST request to /ratings with your favorite HTTP client.
