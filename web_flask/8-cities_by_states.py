#!/usr/bin/python3
"""
Run a simple flask application to query the database
for states and their related cities
"""
from flask import Flask, render_template
from models import storage
from models.state import State
# initiate an application called app
app = Flask(__name__)

@app.teardown_appcontext
def close_session(self):
    """
    This method will close the session after each request
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display states with their cities as per the data
    in the database
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
