#!/usr/bin/python3
"""
start a web application that print "Hello HBNB!"
The application should listen from all network interfaces
on port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    will handle the root URL
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
