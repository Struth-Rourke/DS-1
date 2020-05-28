# salty_app/routes/home_routes.py
import os
import psycopg2
from psycopg2.extras import execute_values
from flask import Blueprint, jsonify
from dotenv import load_dotenv

# env
ENV_PATH = os.path.join(os.getcwd(), '.env')
load_dotenv(ENV_PATH)

# Elephant SQL -- PostgreSQL Credentials
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PW = os.getenv('DB_PW')
DB_HOST = os.getenv('DB_HOST')

# Creating Connection Object
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PW,
                        host=DB_HOST)

# Creating Cursor Object
cursor = conn.cursor()

# Cursor execution
cursor.execute(
    '''
    SELECT DISTINCT author_name
    FROM comments
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
users_routes_test = Blueprint("users_routes_test", __name__)
@users_routes_test.route("/users")
def users():
    return jsonify(author_names)
