#!/usr/bin/python3
"""
start a flask web application listening on 0.0.0.0
port 5000
"""
from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    show the list of states using a Template html
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """
    method to remove current sqlalchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
