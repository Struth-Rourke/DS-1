# salty_app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiating the DataBase from the SQLAlchemy Class
db = SQLAlchemy()

# Instantiating Migrate
migrate = Migrate()


# Defining new class "Tweets": inherents db.model from SQLAlchemy above
class Comments(db.Model):
    # Configuring the attributes, and subsequent DB columns
    comment_id = db.Column(db.BigInteger, primary_key=True)
    author_name = db.Column(db.String, db.ForeignKey("User.author_screen_name"))
    comment_text = db.Column(db.String)
    salty_comment_score_pos = db.Column(db.Float)
    salty_comment_score_neg = db.Column(db.Float)

    # bi-directional association with User model
    user = db.relationship("User", backref=db.backref("Comments", lazy=True))


# Defining new class "User": inherents db.model from SQLAlchemy above
class User(db.Model):
    # Configuring attributes, and subsequent DB columns
    id = db.Column(db.BigInteger, primary_key=True)
    author_screen_name = db.Column(db.String(128), nullable=False)
    user_saltiness_score = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    word_count = db.Column(db.Integer)


# Defining the parse_records function
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into list
    of dictionaries, so they can be returned as JSON.

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
