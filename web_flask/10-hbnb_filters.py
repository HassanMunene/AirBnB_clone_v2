#!/usr/bin/python3
"""
This is a simple web application that is listening
on 0.0.0.0 port 5000
"""
import models
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    display an HBNB page like 6-index.html
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(self):
    """
    close session after each request
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
