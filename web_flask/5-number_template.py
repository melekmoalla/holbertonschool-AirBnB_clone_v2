#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value
of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello1():
    return "HBNB"


@app.route("/c/<text>")
def hello(text):
    a = text.replace("_", " ")
    return f"C {a}"


# @app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello2(text='is cool'):
    b = text.replace("_", " ")
    return f"Python {b}"


@app.route("/number/<int:n>", strict_slashes=False)
def hello3(n):
    if type(n) is int:
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello4(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
