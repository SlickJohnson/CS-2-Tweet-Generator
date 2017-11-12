from flask import Flask, render_template
import sample

import json

from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient('localhost', 27017)

app.db = mongo.test

@app.route('/')
def index():
    if source_word_list is None:
        return "ERROR: NO WORD LIST PROVIDED"

    return render_template('index.html', sentence=sample.get_random_sentence(source_word_list))


if __name__ == "__main__":
    with open("holmes.txt", 'r', encoding='utf8') as source_file:
        source_word_list = [word.lower() for word in source_file.read().rsplit()]

    app.run()
