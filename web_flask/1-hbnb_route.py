#!/usr/bin/python3
"""
create a flask application that listens
on '0.0.0.0' on port 5000
"""
# import the class Flask
from flask import Flask


#initiate an app instance from Flask
app = Flask(__name__)

#define the root url using the route decorator
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    handle the root url
    """
    return "Hello HBNB!"

#define /hbnb route
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    handle /hbnb url
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
