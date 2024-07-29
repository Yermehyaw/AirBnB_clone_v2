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
def c_text(text):
    """
    Return a string using routing text

    Args:
    text(str): routing text

    Return:
    A string with routing text to webpage
    """
    i = 1
    while 1 < len(text):  #/remove undercores
        if text[i] == '_':
            text[i] == ' '
        i += 1
    return f"C {escape(text)}"


@app.route("/python/<text>", strict_slashes=False)
def py_text(text):
    """
    Return a string uaing the routing text/url path
    
   text(str): routing text

    Return:
    A string with routing text to webpage 
    """
    i = 0
    while i < len(text="is cool"):  #/remove undercores
        if text[i] == '_':
            text[i] == ' '
        i += 1
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
