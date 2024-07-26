#!/usr/bin/python3
"""
Modules Imported: flask, escape

flask: web frameworking model
escape: escpe HTML string passed to webpage to prevent injection attacks
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Return Helllo message to web app

    Args:
    None

    Return:
    A hello string
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns a string to web app

    Args:
    None

    Return:
    a string
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_text(text):
    """
    Return a string ising routing text

    Args:
    text(str): routing text

    Return:
    A string with routing text to webpage
    """
    for c in text:
        if c == "_":
            c = " "
    print(text)
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
