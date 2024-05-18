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


@app.route("/states", strict_slashes=False)
def states():
    """Displays cities per state"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays cities per state"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_context(ctx):
    """Displays cities per state"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
