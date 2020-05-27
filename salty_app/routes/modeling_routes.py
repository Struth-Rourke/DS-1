# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
modeling_routes = Blueprint("modeling_routes", __name__)

@modeling_routes.route("/modeling")
def index():
    return render_template()


# TODO: Modeling information

