from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import  DataRequired,Length,Email,Regexp,EqualTo
from wtforms import ValidationError


from ..models import User


class LoginForm(Form):
    """
    登录
    """
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('记住帐号')
    submit = SubmitField('登录 ')


class RegistrationForm(Form):
    """
    注册
    """
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('确认密码',validators=[DataRequired(),EqualTo('password',message='两次密码必须一致')])
    submit = SubmitField('注册')

    def validate_email(self,field):
        """
        邮箱是否被注册
        :param field:
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')

    def validate_username(self,field):
        """
        用户是否被注册
        :param field:
        :return:
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被使用')


