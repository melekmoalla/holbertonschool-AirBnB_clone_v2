#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello1():
    return "HBNB"


@app.route("/c/<text>")
def hello(text):
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
