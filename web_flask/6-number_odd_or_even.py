#!/usr/bin/python3
"""
start a simple flask application
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    handling integer parameter
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    handling integer parameter
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    odd or even number
    """
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"

    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
