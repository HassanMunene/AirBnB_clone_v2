#!/usr/bin/python3
"""
start a flask application that listens on 0.0.0.0
port 5000
"""
# First import the Flask class
from flask import Flask
# instantiate an application using Flask
app = Flask(__name__)


# define the routes for the application using the route decorator
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    handle the root route
    """
    return "Hello HBNH!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    handle the '/hbnb' route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    handle the '/c' route together
    with the variable passed
    """
    text2 = text.replace("_", " ")
    return "c {}".format(text2)


@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    handle the route for pyhthon
    """
    text2 = text.replace("_", " ")
    return "Python {}".format(text2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
