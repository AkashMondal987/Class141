from os import read
from flask import Flask, json, jsonify, request
import csv 
allmovies = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]
likedMovies = []
notLikedMovies = []
didNotWatch = []
app = Flask(__name__)
@app.route("/get-movie")
def getMovie():
    return jsonify({
        "data" : allmovies[0],
        "status" : "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def likedMovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status" : "success"
    }), 201

@app.route("/unliked-movie", methods = ["POST"])
def unlikedMovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notLikedMovies.append(movie)
    return jsonify({
        "status" : "success"
    }), 201

@app.route("/did-not_watch", methods = ["POST"])
def likedMovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    didNotWatch.append(movie)
    return jsonify({
        "status" : "success"
    }), 201

if __name__ == "__main__":
    app.run()