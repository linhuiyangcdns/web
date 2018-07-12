from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user

from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from app import db
# from ..email import send_email
#
# @auth.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.ping()
#         if not current_user.confirmed \
#                 and request.endpoint \
#                 and request.endpoint[:5] != 'auth.' \
#                 and request.endpoint != 'static':
#             return redirect(url_for('auth.unconfirmed'))

# @auth.route('/unconfirmed')
# def unconfirmed():
#     if current_user.is_anonymous or current_user.confirmed:
#         return redirect(url_for('main.index'))
#     return render_template('auth/email/unconfirmed.html')



@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经成功退出退出了.')
    return redirect(url_for('main.index'))


@auth.route('/register',methods=['GET','POST'])
def register():
    """
    注册
    :return:
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
            db.session.add(user)
            # db.session.commit()  # 这里不能等数据库自动保存，因为用户在验证时需要登录
            # token = user.generate_confirmation_token()  # 生成HASH码
            # send_email(user.email, '确认你的账户',
            #            'auth/email/confirm', user=user, token=token)  # 发送验证信息
            # flash('邮件已经发送！')
            flash('注册成功')
            return redirect(url_for('auth.login'))
        except:
            flash('帐号已经存在')
            return redirect(url_for('auth.register'))
    return render_template('auth/register.html',form=form)













# @auth.before_app_request
# def before_app_request():
#     if current_user.is_authenticated():
#         current_user.ping()
#         if not current_user.c





# @auth.route('/confirm/<token>')
# @login_required
# def confirm(token):
#     """
#     邮箱确认
#     :param token:
#     :return:
#     """
#     if current_user.confirmed:
#         return redirect(url_for('main.index'))
#     if current_user.confirm(token):
#         flash('你已经确认了你的账户。谢谢!')
#     else:
#         flash('确认链接无效或已过期。')
#     return redirect(url_for('main.index'))
#
#
# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email(current_user.email, '确认你的账户',
#                'auth/email/confirm', user=current_user, token=token)
#     flash('一封新的确认邮件已经通过电子邮件发送给你了.')
#     return redirect(url_for('main.index'))



