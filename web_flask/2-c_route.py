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
    Return a string ising routing text

    Args:
    text(str): routing text
    
    Decription:
    A more advanced methid of chnging URL underscores
    to whitespaces would be:

    from werkzeug.routing import BaseConverter
    class = UnderscoreConverter(BaseConverter):
        def remove_underscores(self, value):
            return value.replace('_', ' ')
    app.url_map.converters['underscore'] = UnderscoreConverter
    
    @app.route('/c/<underscore: text>', strict_slashes=False)
    def c_text:
    . . . 


    Return:
    A string with routing text to webpage
    """
    i = 0
    while i < len(text):  #/remove undercores
        if text[i] == '_':
            text[i] == ' '
        i += 1
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
