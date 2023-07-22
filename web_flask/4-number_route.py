#!/usr/bin/python3
"""
create a flask application that listens on 0.0.0.0
port 5000
"""
# firstly we need to import the class Flask
from flask import Flask
# then instantiate an application using the Flask class
app = Flask(__name__)


# define the routes for the application
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    handle the "/" route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    handle the route for "/hbnb"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Handle the "c/<text>" route
    """
    return "C is {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': "is fun"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    handle the two routes both the default root
    and the route with a variable provided
    """
    text2 = text.replace("_", " ")
    return "Python {}".format(text2)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    handle the '/number/<n>' route
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

