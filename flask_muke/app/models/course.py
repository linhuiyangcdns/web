from app import db
from werkzeug.security import generate_password_hash,check_password_hash  # 密码散列
from flask_login import UserMixin,AnonymousUserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from .. import db

class Course(db.Model):
    pass