from app import db
from werkzeug.security import generate_password_hash,check_password_hash  # 密码散列
from flask_login import UserMixin,AnonymousUserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from .. import db


class UserProfile(db.Model):
    """
    用户
    """
    __tablename__ = 'users'
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64),unique=True,index=True)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(6),default='female')
    address = db.Column(db.String(100))
    mobile = db.Column(db.String(11))


