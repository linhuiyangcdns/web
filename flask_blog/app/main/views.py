from flask import render_template,abort,redirect,flash,url_for
from flask_login import login_required,current_user

from . import main
from ..models import User,Post,Comment
from .forms import EditProfileForm,PostForm,CommentForm
from app import db
from datetime import datetime

@main.route('/',methods=['GET','POST'])
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html',posts=posts)


@main.route('/user/<username>',methods=['GET','POST'])
def user(username):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.titile.data,body=form.body.data,author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user).all()

    if user is None:
        abort(404)
    return render_template('user.html',user=user,form=form,posts=posts)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('您的个人资料已经更新.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/<username>/article/<title>',methods=['GET','POST'])
def article(username,title):
    user = User.query.filter_by(username=username).first()
    post = Post.query.filter_by(title=title).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,timestamp=datetime.utcnow(),post=post,author=current_user._get_current_object())
        db.session.add(comment)
        flash('提交成功')
        return redirect(url_for('main.article',username=user.username,title=post.title))
    comments = post.comments.order_by(Comment.timestamp.desc()).all()
    return render_template('article.html',user=user,post=post,form=form,comments=comments)

@main.route('/notlogin')
def not_login():
    return render_template('notlogin.html')
