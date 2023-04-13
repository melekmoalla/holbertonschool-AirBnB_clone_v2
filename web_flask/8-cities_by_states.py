#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

@app.route("/cities_by_states", strict_slashes=False)
def cities():

    states = storage.all(State).values()
    cities = storage.all(City).values()



    return render_template('8-cities_by_states.html', city=cities, states=states)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)