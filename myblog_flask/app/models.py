from app import db
from werkzeug.security import generate_password_hash,check_password_hash  # 密码散列
from flask_login import UserMixin
from . import login_manager
from datetime import datetime




class Role(db.Model):
    """
    角色
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(db.Integer)
    users = db.relationship('User',backref=db.backref('role',lazy='dynamic'))

    def __repr__(self):
        return '<Role %r>' % self.name

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model,UserMixin):
    """
    用户
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')
    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')


    @property
    def password(self):
        raise ArithmeticError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    """
    文章
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),index=True)
    body = db.Column(db.Text)
    created_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    categories_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    comments = db.relationship('Comment',backref='post',lazy= 'dynamic')
    tag_id = db.relationship('Tag',backref=db.backref('post', lazy='dynamic'))

    def __repr__(self):
        return '<Post %r > ' % self.title


class Tag(db.Model):
    """
    标签
    """
    __tablename__ = 'tags'
    id = db.Column(db.String(45),primary_key=True)
    name = db.Column(db.String(255))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))


    def __repr__(self):
        return '<Tag %r >' % self.name


class Category(db.Model):
    """
    分类
    """
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    post_id = db.relationship('Post',backref='categories',lazy='dynamic')

    def __repr__(self):
        return '<Category %r' % self.name


class Comment(db.Model):
    """
    评论
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __repr__(self):
        return '<Commet %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

