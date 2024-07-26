"""
Modules Imported: flask

flask: web frameworking model
"""
from flask import Flask


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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
