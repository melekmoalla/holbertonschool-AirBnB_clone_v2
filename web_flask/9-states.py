#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/states")
def states(id=None):
    states = storage.all(State)()
    states_sorted = []
    for state_id in sorted(states):
        state = states[state_id]
        states_sorted.append(state)
    return render_template('7-states_list.html',  states=states_sorted, id=id)


@app.route("/states/<id>")
def satates_id(id=None):
    states = storage.all(State)
    cities = storage.all(City)
    key = "State."+id
    states_sorted = states[key]

    cytys = []
    for citie in sorted(cities):
        city = cities[citie]
        if city.state.id == id:
            cytys.append(city)
    return render_template('9-states.html', city=cytys, states=states_sorted, id=id)


@app.teardown_appcontext
def teardown_appcontext(ex):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
