import os
from flask import Flask
from dotenv import load_dotenv
from salt_test_app.models_t import db, migrate
from salt_test_app.routes.home_routes_test import home_routes_test
from salt_test_app.routes.modeling_routes import modeling_routes
from salt_test_app.routes.stats_routes import stats_routes
from salt_test_app.routes.users_routes_test import users_routes_test


# Creating DataBase name in the current directory -- using relative filepath
load_dotenv()
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")


# Defining Function "create_app"
def create_app():
    # Instantiating Flask App
    app = Flask(__name__)

    # Configures the DataBase w/ name specified by "DATABASE_URI"
    app.config["SQLALCHEMY_DATABASE_URI"] = TEST_DATABASE_URL
    # Initializes the DataBase
    db.init_app(app)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints from the different routes
    app.register_blueprint(home_routes_test)  # ("/home")
    app.register_blueprint(modeling_routes)  # ("/modeling")
    app.register_blueprint(stats_routes)  # ("/stats")
    app.register_blueprint(users_routes_test)  # ("/user")

    # Returning / Running Flask App
    return app


# Factory pattern; Flask best practice -- creating and running app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
