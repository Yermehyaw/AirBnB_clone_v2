#!/usr/bin/python3
"""
Modules Imported: flask, escape

flask: web frameworking model
escape: escpe HTML string passed to webpage to prevent injection attacks
"""
from flask import Flask, render_template
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
    no_underscore = text
    no_underscore = no_underscore.replace('_', ' ')
    return f"C {escape(no_underscore)}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text):
    """
    Return a string using a  specified routing text/url path

    text(str): routing text

    Return:
    A string with routing text to webpage
    """
    no_underscore = text
    no_underscore = no_underscore.replace('_', ' ')
    return f"Python {escape(no_underscore)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """
    Return a string with route text applying flask varible rules

    Args:
    n(int): an positive integer. No decimal points

    Return:
    A string with the routung text to the webpage
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_page(n):
    """
    Return a jinja2 template with a routing text/arg

    Args:
    n(int): an positive integer. No decimal points

    Return:
    A html page from  a rendered jinja2 template
    """
    return render_template("5-nunber.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
