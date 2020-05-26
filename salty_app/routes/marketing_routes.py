# twitter_app/routes/home_routes.py

from flask import Blueprint, render_template

# Instantiate new blueprint object
marketing_routes = Blueprint("marketing_routes", __name__)

@marketing_routes.route("/marketing")
def index():
    return render_template()