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


@app.route("/c/<text>", strict_slashes=False)
def dynamic_c_route(text):
    """/dynamic c route : dispaly HBNB"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def dynamic_python_route(text="is cool"):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
