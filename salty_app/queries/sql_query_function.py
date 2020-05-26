# Defining "comment table" function 
def create_comment_table(cursor, conn):
    print("-----------------")
    print("CREATING TABLE IN THE DATABASE...")

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS salty_db (
            comment_id INT,
            author_id INT,
            author_name VARCHAR,
            comment_text VARCHAR,
            salty_comment_score FLOAT,
            PRIMARY KEY (comment_id)
            FOREIGN KEY (id)
            )
            '''
    cursor.execute(create_table_query)
    conn.commit()


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

