# salty_app/routes/home_routes.py
import os
import psycopg2
from psycopg2.extras import execute_values
from flask import Blueprint, render_template, jsonify
from dotenv import load_dotenv

# env
ENV_PATH = os.path.join(os.getcwd(), '.env')
load_dotenv(ENV_PATH)

# Elephant SQL -- PostgreSQL Credentials
ELE_DB_USER = os.getenv('ELE_DB_USER')
ELE_DB_NAME = os.getenv('ELE_DB_NAME')
ELE_DB_PW = os.getenv('ELE_DB_PW')
ELE_DB_HOST = os.getenv('ELE_DB_HOST')

# Creating Connection Object
conn = psycopg2.connect(dbname=ELE_DB_NAME,
                        user=ELE_DB_USER,
                        password=ELE_DB_PW,
                        host=ELE_DB_HOST)

# Creating Cursor Object
cursor = conn.cursor()

# Cursor execution
cursor.execute(
    '''
    SELECT DISTINCT author_name
    FROM salty_db_2
    GROUP BY author_name
    ''')
# List of cursor.execute assigned to a variable
authors = list(cursor.fetchall())
# Instantiating empty list
author_names = []
# Counter
counter = 0
# For Loop for author in authors
for author in authors:
    author = authors[counter][0]
    author_names.append(author)
    counter += 1


# Closing Connection
conn.close()
# Instantiate new blueprint object
users_routes = Blueprint("users_routes", __name__)
@users_routes.route("/users")
def users():
    return jsonify(author_names)
