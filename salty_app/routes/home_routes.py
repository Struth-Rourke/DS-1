# salty_app/routes/home_routes.py
import requests
import html
import re
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
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

cursor.execute(
    '''
    SELECT *
    FROM salty_db_2
    ''')
comments = list(cursor.fetchall())
data = comments
# counter = 0
# for comment in comments:
#     comment = comments[counter]
#     data.append(comment)
#     counter += 1


# Instantiate new blueprint object
home_routes = Blueprint("home_routes", __name__)
@home_routes.route("/home")
def data_function():
    print("DATA Type:", type(data))
    return jsonify(data)
