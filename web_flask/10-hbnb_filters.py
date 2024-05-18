#!/usr/bin/python3
"""
route  :   /hbnb_filters: display a HTML page like 6-index.html,
which was done during the project 0x01. AirBnB clone - Web static

"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


app.debug = True


@app.teardown_appcontext
def teardown_context(ctx):
    """Displays cities per state"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
