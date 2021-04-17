"""
Phonic Application Factory.

Handles
-------
- App Configuration
- Registering Flask plug ins
- Registering Blueprints

"""
# Standard Imports.
import os

# Flask Imports.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init Configurations.
DATABASE_NAME = "phonic_db.sql"
db = SQLAlchemy()
ma = Marshmallow()


def create_app(test_config=None):
    """
    Application Factory.

    Parameters
    ----------
    test_config: dict, default=None.
        Test Configuration.

    Returns
    -------
    app: object.
        Flask Application Instance.
    """

    # Init Flask app.
    app = Flask(import_name=__name__,
                instance_relative_config=True)  # Set Production Config to point to instance folder.

    # Grab Database path.
    root_dir = os.path.abspath(os.path.dirname(__file__))
    database_uri = "sqlite:///" + os.path.join(root_dir, DATABASE_NAME)

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=database_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Handle Production vs Development Config.
    if test_config is None:
        # Load from instance_folder/config.py.
        app.config.from_pyfile(filename="config.py",
                               silent=True)
    else:
        # Load from config given.
        app.config.from_mapping(test_config)

    # Ensure instance_folder/ exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "Hello, World!"

    return app
