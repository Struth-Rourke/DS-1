import requests
import html
import re
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
from dotenv import load_dotenv
# ENV_PATH = os.path.join(os.getcwd(), '.env')
load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PW = os.getenv('DB_PW')
DB_HOST = os.getenv('DB_HOST')
conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PW,
                        host=DB_HOST)
cursor = conn.cursor()
cursor.execute(
    '''
    SELECT DISTINCT author_name
    FROM "comments"
    GROUP BY author_name
    ''')
authors = list(cursor.fetchall()) #> Gets list of author name tuples
author_names = []
counter = 0
for author in authors:
    author = authors[counter][0]
    author_names.append(author) # Tries to get author string for each author, but only gets the first author several times
    counter += 1
breakpoint()