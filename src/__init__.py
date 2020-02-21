from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, DDL

from src.configuration.config import FlaskConfig


db = SQLAlchemy()


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    # database
    db.init_app(app)

    # apply the blueprints to the app
    from src.cedric import CedricController
    from src.greet import GreetController

    app.register_blueprint(GreetController.bp)
    app.register_blueprint(CedricController.bp)

    with app.app_context():

        # Create tables for our models
        db.create_all()

        return app
