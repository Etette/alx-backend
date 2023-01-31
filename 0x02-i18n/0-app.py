#!/usr/bin/env python3
"""
Flask app
First you will setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template that
simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>).
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)