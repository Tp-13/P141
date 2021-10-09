from flask import Flask, app, jsonify, request
import csv

all_articles = []
with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

like_articles = []
unlike_articles = []
app = Flask(__name__)
@app.route("/get-articles")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    like_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unlike_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()