from flask import Flask, render_template
import sample

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', sentence=sample.get_random_sentence('holmes.txt'))


if __name__ == "__main__":
    app.run()
