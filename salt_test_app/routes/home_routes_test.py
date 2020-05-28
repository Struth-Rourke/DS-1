# salty_app/routes/home_routes.py
import os
import psycopg2
from psycopg2.extras import execute_values
from flask import Blueprint, jsonify
from dotenv import load_dotenv
import pandas as pd

# env
ENV_PATH = os.path.join(os.getcwd(), '.env')
load_dotenv(ENV_PATH)

# Elephant SQL -- PostgreSQL Credentials
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PW = os.getenv('DB_PW')
DB_HOST = os.getenv('DB_HOST')


def fetch_query_comments(query):
    # Creating Connection Object
    conn = psycopg2.connect(dbname=DB_NAME,
                            user=DB_USER,
                            password=DB_PW,
                            host=DB_HOST)
    # Creating Cursor Object
    cursor = conn.cursor()
    # Fetch comments query
    query = query
    # Execute query
    cursor.execute(query)
    # Query results
    comments = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["comment_id",
               "username",
               "comment_text",
               "score_pos",
               "score_neg"]
    # List of tuples to DF
    df = pd.DataFrame(comments, columns=columns)
    print(type(df))
    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    conn.close()

    return pairs


# Instantiate new blueprint object
home_routes_test = Blueprint("home_routes_test", __name__)

# Index Route
@home_routes_test.route("/")
def index():
    return """<xmp>
    WELCOME TO SALTIEST!
    \n
    YOU ARE CURRENTLY IN THE DATA LANDING PAGE. SEE BELOW FOR RETRIEVAL INSTRUCTIONS.
    \n
    \n
    \n
    VISIT THE FOLLOWING ADDRESSES TO RETRIEVE KEY VALUE PAIR DATA(Local):
    \n
    http://localhost:5000/home
    \n
    http://localhost:5000/top20_saltiest_users
    \n
    http://localhost:5000/top20_sweetest_users
    \n
    http://localhost:5000/top10_commenters
    \n
    http://localhost:5000/top100_salty_comments
    \n
    http://localhost:5000/top100_sweetest_comments
    \n
    \n
    \n
    VISIT THE FOLLOWING ADDRESSES TO RETRIEVE KEY VALUE PAIR DATA(Heroku):
    \n
    https://saltyapp.herokuapp.com/home
    \n
    https://saltyapp.herokuapp.com/top20_saltiest_users
    \n
    https://saltyapp.herokuapp.com/top20_sweetest_users
    \n
    https://saltyapp.herokuapp.com/top10_commenters
    \n
    https://saltyapp.herokuapp.com/top100_salty_comments
    \n
    https://saltyapp.herokuapp.com/top100_sweetest_comments
    </xmp>"""
    

@home_routes_test.route("/home")
def data_function():
    query = """
    SELECT *
    FROM comments
    """
    return fetch_query_comments(query)



### NOTES ON DATA:
# type(data): list
# type(data[0]): tuple
# data[0][0]: comment id
# data[0][1]: username
# data[0][2]: comment text
# data[0][3]: score pos
# data[0][4]: score neg


####################### Queries: #######################

# # COMMENT COUNT PER USER -

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



# # TOP 10 COMMENTERS (FREQUENCY) -

# cursor.execute(
#     '''
#     SELECT 
# 	    COUNT(DISTINCT comment_id) as comment_count,
# 	    author_name
#     FROM salty_db_2
#     GROUP BY author_name
#     ORDER BY comment_count DESC
#     LIMIT 10
#     '''
# )



# # TOP 100 SALTIEST COMMENTS -

# cursor.execute(
#     '''
#     SELECT *
#     from salty_db_2
#     WHERE salty_comment_score_neg > 0 -- to exclude nulls
#     ORDER BY salty_comment_score_neg DESC
#     LIMIT 100
#     '''
# )



# # AVG SALTY COMMENT SCORE PER USER -

# cursor.execute(
#     '''
#     SELECT 
#         AVG(salty_comment_score_neg) as avg_salty_score,
#         author_name,
# 	    COUNT (DISTINCT comment_id) as comment_count
#     FROM salty_db_2
#     WHERE salty_comment_score_neg > 0
#     GROUP BY author_name
#     ORDER BY AVG(salty_comment_score_neg) DESC
#     '''
# ) 
# #> This outputs an avg saltiness score as well as 
# # comment count. The "saltiest" averages came from 
# # users with only 1 comment ... need to 
# # establish threshold / baseline?



# # AVG COMMENT COUNT - 

# cursor.execute(
#     '''
#     SELECT
#         AVG(comment_count)
#     FROM (
#         SELECT 
#             COUNT (DISTINCT comment_id) as comment_count
#             , author_name
#         from salty_db_2
#         GROUP BY author_name
#         ORDER BY comment_count DESC
#     ) AS comment_query -- had to assign the subquery an alias for some reason
#     '''
# )

# #> Output is 2.35



# # TOP TEN SALTIEST COMMENTERS (AT LEAST 3 COMMENTS MADE) -

# cursor.execute(
#     '''
#     SELECT *
#     FROM (
#         SELECT
#             AVG(salty_comment_score_neg) as avg_salty_score,
#             author_name,
#             COUNT (DISTINCT comment_id) as comment_count
#         FROM salty_db_2
#         WHERE salty_comment_score_neg > 0
#         GROUP BY author_name
#         ORDER BY avg_salty_score DESC
#     ) AS comment_query
#     WHERE comment_count > 2
#     LIMIT 10
#     '''
# )

# #> This output includes avg salty score, author name, and comment
# # count (greater than 2, since avg num of comments is 2.35).
# # For reference, highest avg saltiness score here was 0.318 from
# # Chris2048 with 3 comments