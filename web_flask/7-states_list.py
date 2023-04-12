#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def diplay():
    states = storage.all(State).values()
    states_sorted = []
    for state_id in sorted(states):
        state = states[state_id]
        states_sorted.append(state)

    return render_template('7-states_list.html', states=states_sorted)


@app.teardown_appcontext
def teardown_appcontext(ex):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
