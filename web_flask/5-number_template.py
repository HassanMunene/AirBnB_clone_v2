#!/usr/bin/python3
"""
run a flask web application that listens on 0.0.0.0
port 5000
"""
# we need to import the Flask class first
from flask import Flask
from flask import render_template
# then instantiate our application using the class
app = Flask(__name__)


# define the routes that the application will server when running
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    handle the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    handle the /hbnb route here
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    handle the route with its variable
    """
    text2 = text.replace("_", " ")
    return f"C {text2}"


@app.route("/python/", defaults={'text': "is fun"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    handle both the routes
    """
    text2 = text.replace("_", " ")
    return f"python {text2}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    handel only integer variable
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """
    handle the route to render template
    if the variable provided is an integer
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
