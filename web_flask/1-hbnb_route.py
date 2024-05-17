#!/usr/bin/python3
""" module serves as a flask starter and makeing another page"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """/hbnb route : dispaly HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
