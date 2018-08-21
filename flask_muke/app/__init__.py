from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager
from app.database import db
from flask import current_app


from app.operation import operation
from app.auth import auth


bootstrap = Bootstrap()
email = Mail()
login_manager = LoginManager()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)
    register_blueprints(app)


    return app

def register_extensions(app):
    """ Register extensions with the Flask application."""

    db.init_app(app)
    bootstrap.init_app(app)
    email.init_app(app)


def register_blueprints(app):
    """ Register blueprints with the Flask application."""
    app.register_blueprint(operation)
    app.register_blueprint(auth, url_prefix='/auth')