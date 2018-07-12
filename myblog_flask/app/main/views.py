from datetime import datetime
from flask import render_template, sessions, redirect, url_for
from sqlalchemy import func


from ..models import db,User,Post,Tag,Comment
from . import main


# def sidebar_data():
#     """
#     右边标签内最近文章和标签排行
#     """
#     recent = Post.query().order_by(Post.created_time.desc()).limit(5).all()
#     top_tags =  db.session.query(Tag,func.count(Post.id).label('total')).group_by(Tag).order_by('total DESC').limit(5).all()
#     return recent,top_tags


@main.route('/index',methods=['GET'])
def index():
    posts = db.session.query(Post).order_by(Post.created_time.desc()).all()
    return render_template('index.html', post=posts)


