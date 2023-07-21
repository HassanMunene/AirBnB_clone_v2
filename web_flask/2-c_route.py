#!/usr/bin/python3
"""
start a flask application that listens on 0.0.0.0
on port 5000
"""
# we need to import the class Flask
from flask import Flask

# create an app instance from Flask
app = Flask(__name__)


# define the root url
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    define the root url function
    """
    return "Hello HBNB!"


# define '/hbnb' url route
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    define what the '/hbnb' url does
    """
    return "HBNB"


# define "/c/<text>" url route
@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    will handle the route with the variable too
    """
    text2 = text.replace("_", " ")
    return "C {}".format(text2)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
