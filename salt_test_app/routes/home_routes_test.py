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
#         from salty_db_2
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