import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

ELE_DB_USER = os.getenv("ELE_DB_USER")
ELE_DB_NAME = os.getenv("ELE_DB_NAME")
ELE_DB_PW = os.getenv("ELE_DB_PW")
ELE_DB_HOST = os.getenv("ELE_DB_HOST")


# Create connection to ElephantSql database
def create_cursor(ELE_DB_USER, ELE_DB_NAME, ELE_DB_PW, ELE_DB_HOST):
    conn = psycopg2.connect(
                            dbname=ELE_DB_NAME,
                            user=ELE_DB_USER,
                            password=ELE_DB_PW,
                            host=ELE_DB_HOST
                            )
    cursor = conn.cursor()
    return cursor


if __name__ == "__main__":
    cursor = create_cursor(ELE_DB_USER, ELE_DB_NAME, ELE_DB_PW, ELE_DB_HOST)
    print(type(cursor))
