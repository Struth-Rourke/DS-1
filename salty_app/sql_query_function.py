import psycopg2
from psycopg2.extras import execute_values


def create_user_table(cursor, conn):
    print("-----------------")
    print("CREATING TABLE IN THE DATABASE...")

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS salty_user_db (
            id INT,
            author_screen_name VARCHAR,
            user_saltiness_score INT,
            comment_count INT,
            word_count INT,
            PRIMARY KEY (id)
            )
            '''
    cursor.execute(create_table_query)
    conn.commit()


# Defining "comment table" function 
def create_comment_table(cursor, conn):
    print("-----------------")

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS salty_db_2 (
            comment_id INT,
            author_name VARCHAR,
            comment_text VARCHAR,
            salty_comment_score_pos FLOAT,
            salty_comment_score_neg FLOAT,
            PRIMARY KEY (comment_id)
            )
            '''
    cursor.execute(create_table_query)
    conn.commit()


def populate_comment_table_query(cursor, conn, i, item_json, maxitem):
    query = f'''
        SELECT
            comment_id
        FROM salty_db_2
        WHERE comment_id={maxitem}
        '''
    cursor.execute(query)
    record = cursor.fetchone()
    if record is None:
        print(f'Adding comment with id {maxitem} to database')
        # The record isn't found in the database
        # add the record to the database
        query = '''
        INSERT INTO salty_db_2 (comment_id, author_name, comment_text)
        VALUES %s
        '''
        execute_values(
            cursor,
            query,
            [
                (
                    str(item_json['id'])
                    ,item_json['by']
                    ,item_json['text']
                )
            ]
        )
        conn.commit()
        i+=1
    else:
        # The record is already in the database
        # Alert the console
        print(f"WARNING: Duplicate entry {maxitem} found in database!")
    return i, maxitem
