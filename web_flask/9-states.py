#!/usr/bin/python3
"""
run a simple flask application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """
    close sqlalchemy session after each request
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    display the states
    """
    states = storage.all('State')
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
    show the city of that specified state
    """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
