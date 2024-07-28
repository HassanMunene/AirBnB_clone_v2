#!/usr/bin/python3
"""
start a simple flask application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def awesome_c(text):
    """
    how to handle parameters in a route
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def awesome_python(text):
    """
    handle parameters and default values
    """
    text = text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
