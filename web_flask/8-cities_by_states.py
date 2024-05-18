#!/usr/bin/python3
"""
A script to To load all cities of a State,
If storage engine is DBStorage, use cities relationship
Otherwise, use the public getter method cities.
After each request remove the current SQLAlchemy Session,
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """A function that serves as the home route of the application.
    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays cities per state"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_context(ctx):
    """Displays cities per state"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
