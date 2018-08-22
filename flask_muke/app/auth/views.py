from . import auth
from flask import render_template, flash, redirect, request, session, url_for,make_response
from flask_login import login_user,logout_user,login_required,current_user
from .forms import RegisterForm, LoginForm, FindPasswordForm, ResetPasswordForm,get_verify_code
import time
from app.users.models import User
from app.database import db



# 注册
@auth.route('/register/', methods=["POST", 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if session.get('image') != form.verify_code.data:
            flash('验证码错误','yzmerror')
            return redirect(url_for('auth.register'))
        try:
            user = User(email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            flash('注册成功','result')
            return redirect(url_for('auth.login'))
        except:
            flash('帐号已经存在','exists')
            return redirect(url_for('auth.register'))
    return render_template('auth/register.html', form=form)


# 登陆
@auth.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if session.get('image') != form.verify_code.data:
            flash('验证码错误','yzm')
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('operation.index'))
        else:
            flash('用户名或者密码不正确','zhmm')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)



# 找回密码
@auth.route('/forgetpwd', methods=["POST", "GET"])
def forgetpwd():
    form = FindPasswordForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["username"])
        print(request.form["email"])
        return redirect(url_for('auth.password_reset'))
    else:
        return render_template('auth/forgetpwd.html', form=form)


# 重置密码
@auth.route('/password_reset', methods=["POST", "GET"])
def password_reset():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["password"])
        print(request.form["re_password"])
        return "重置密码"
    else:
        return render_template('auth/password_reset.html', form=form)


# 修改密码
@auth.route('/changepwd', methods=["POST", "GET"])
def changepwd():
    pass


from io import BytesIO


@auth.route('/code')
def get_code():
    image, code = get_verify_code()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    return response