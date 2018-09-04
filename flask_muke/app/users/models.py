from app.database import db
import hashlib
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import time



class User(db.Model):
    """
    用户
    """
    __tablename__ = 'users'
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(6),default='female')
    address = db.Column(db.String(100))
    mobile = db.Column(db.String(11),unique=True)
    password = db.Column(db.String(256))
    pwd = db.Column(db.String(256))
    password_hash = db.Column(db.String(128), unique=True)  # 密码 哈希
    avatar_hash = db.Column(db.String(32))
    image = db.Column(db.Text)  # 图像
    ac_type = db.Column(db.String(4), default="1")  # 1表示普通用户 2表示管理员后台账号
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(1024))



    def check_pwd(self, password):  # 检验密码
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)



    def __repr__(self):
        return '<User %r>' % self.username