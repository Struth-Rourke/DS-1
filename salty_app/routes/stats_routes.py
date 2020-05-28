# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/top")
def index():
    return render_template()

# TODO: All the DB info
