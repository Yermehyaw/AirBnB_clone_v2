#!/usr/bin/python3
"""
Modules Imported: flask, escape

flask: web frameworking model
escape: escpe HTML string passed to webpage to prevent injection attacks
"""
from flask import Flask
from flask import render_template
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
    i = 1
    while 1 < len(text="is cool"):  #/remove undercores
        if text[i] == '_':
            text[i] == ' '
        i += 1
    return f"Python {escape(text)}"


app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """
    Return a string with route text applying flask varible rules
    
    Args:
    n(int): an positive integer. No decimal points
    
    Return:
    A string with the routung text to the webpage
    """
    return f"{escape(n)} is a number"


app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_text(n):
    """
    Return a jinja2 template with a routing text/arg
    
    Args:
    n(int): an positive integer. No decimal points
    
    Return:
    A html page from  a rendered jinja2 template
    """
    return render_template("5-nunber.html", n=n)


app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_page(n):
    """
    Return a webpage indicating if n is odd or even
    
    Args:
    n(int): an positive integer. No decimal points
    
    Return:
    A html page from  a rendered jinja2 template
    
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
