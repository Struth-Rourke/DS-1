# # salty_app/__init__.py
# import requests
# import html
# import re
# import os
# import pandas as pd
# import psycopg2
# from psycopg2.extras import execute_values
# from sqlalchemy import create_engine
# from dotenv import load_dotenv




import os
from dotenv import load_dotenv
load_dotenv()

# Importing Flask that allows you to make the app
from flask import Flask

# Importing necessary classes, packages, variables, etc. from different routes
from salty_app.models import db, migrate
from salty_app.routes.aboutus_routes import aboutus_routes
from salty_app.routes.home_routes import home_routes
from salty_app.routes.marketing_routes import marketing_routes
from salty_app.routes.modeling_routes import modeling_routes
from salty_app.routes.stats_routes import stats_routes
from salty_app.routes.user_routes import user_routes

# ENV_PATH = os.path.join(os.getcwd(), '.env')
# load_dotenv(ENV_PATH)


# ELE_DB_USER = os.getenv('ELE_DB_USER')
# ELE_DB_NAME = os.getenv('ELE_DB_NAME')
# ELE_DB_PW = os.getenv('ELE_DB_PW')
# ELE_DB_HOST = os.getenv('ELE_DB_HOST')

# conn = psycopg2.connect(dbname=ELE_DB_NAME, 
#                         user=ELE_DB_USER,
#                         password=ELE_DB_PW,
#                         host=ELE_DB_HOST)

# cursor = conn.cursor()

# Creating DataBase name in the current directory -- using relative filepath
DATABASE_URL = os.getenv("DATABASE_URL")


# Defining Function "create_app"
def create_app():
    # Instantiating Flask App
    app = Flask(__name__)

    # Configures the DataBase w/ name specified by "DATABASE_URI"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # Initializes the DataBase
    db.init_app(app)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints from the different routes
    app.register_blueprint(aboutus_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(marketing_routes)
    app.register_blueprint(modeling_routes)
    app.register_blueprint(stats_routes)
    app.register_blueprint(user_routes)    
    
    # Returning / Running Flask App
    return app





# Factory pattern; Flask best practice -- creating and running app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)