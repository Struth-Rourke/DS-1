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

# Cursor Object
cursor.execute(
    '''
    SELECT *
    FROM comments
    ''')
# List of cursor.execute assigned to a variable
comments = list(cursor.fetchall())
# Setting comments variable to data variable
data = comments


# Closing Connection
conn.close()


# Instantiate new blueprint object
home_routes_test = Blueprint("home_routes_test", __name__)
@home_routes_test.route("/home")
def data_function():
    print("DATA Type:", type(data))
    return jsonify(data)


### Queries:

# # Comment Count -
# cursor.execute(
#     '''
#     SELECT 
# 	    COUNT(DISTINCT comment_id) as comment_count,
# 	    author_name
#     FROM salty_db_2
#     GROUP BY author_name
#     ORDER BY comment_count DESC
#     '''
# )

# # Top 100 Saltiest Comments -
# cursor.execute(
#     '''
#     SELECT *
#     from salty_db_2
#     WHERE salty_comment_score_neg > 0 -- to exclude nulls
#     ORDER BY salty_comment_score_neg DESC
#     LIMIT 100
#     '''
# )

