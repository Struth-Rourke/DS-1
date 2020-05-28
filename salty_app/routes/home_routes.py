# salty_app/routes/home_routes.py
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from flask import Blueprint, jsonify
from dotenv import load_dotenv
from salty_app.sql_query_function import fetch_query_comments


# Instantiate new blueprint object
home_routes = Blueprint("home_routes", __name__)
@home_routes.route("/home")
def data_function():
    query = '''
    SELECT *
    FROM salty_db_2
    '''
    
    return fetch_query_comments(query)
