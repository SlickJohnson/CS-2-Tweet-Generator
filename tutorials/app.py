from flask import Flask
import sample

app = Flask(__name__)


@app.route('/')
def hello_world():
    return sample.get_random_sentence('holmes.txt')


if __name__ == "__main__":
    app.run()
