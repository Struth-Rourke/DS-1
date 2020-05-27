# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users")
def index():
    return render_template()

# TODO: User information
