# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return 2 + 2 = 4