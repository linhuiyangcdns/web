from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_mail import Mail

import pymysql
pymysql.install_as_MySQLdb()

bootstrap = Bootstrap()
db = SQLAlchemy()
email = Mail()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    email.init_app(app)

    from .operation import operation as operation_blueprint
    app.register_blueprint(operation_blueprint)


    return app