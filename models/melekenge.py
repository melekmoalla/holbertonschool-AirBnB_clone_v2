#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""


from models import storage
from models.state import State
from models.city import City


def diplay():
    storage = FileStorage()
    states = storage.all(State).values()
    states_sorted = []
    for state_id in sorted(states):
        state = states[state_id]
        states_sorted.append(state)

diplay()