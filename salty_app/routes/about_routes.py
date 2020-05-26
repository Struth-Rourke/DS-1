# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
about_routes = Blueprint("about_routes", __name__)

@about_routes.route("/about")
def index():
    return render_template()