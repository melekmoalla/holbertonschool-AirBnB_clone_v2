#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities():

    states = storage.all(State)
    cities = storage.all(City)
    states_sorted = []
    for state_id in sorted(states):
        state = states[state_id]
        states_sorted.append(state)
    cytys = []
    for citie in sorted(cities):
        city = cities[citie]
        cytys.append(city)

    return render_template('8-cities_by_states.html', city=cytys, states=states_sorted)


@app.teardown_appcontext
def teardown_appcontext(ex):
    storage.close()
