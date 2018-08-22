from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextField, DateField, PasswordField,BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, Regexp,EqualTo,Length
from wtforms import ValidationError
from app.users.models import User


# 注册
class RegisterForm(Form):
    email = StringField("邮箱",validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField("密码",validators=[DataRequired()])
    re_password = PasswordField("再次输入密码",validators=[DataRequired(),EqualTo('password',message='两次密码必须一致')])
    verify_code = StringField('VerifyCode', validators=[DataRequired()])
    submit = SubmitField("注册")

    def validate_email(self, field):
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


# 登陆
class LoginForm(Form):
    email = StringField("邮箱",validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField("密码",validators=[DataRequired()])
    verify_code = StringField('VerifyCode', validators=[DataRequired()])
    remember_me = BooleanField('记住帐号')
    submit = SubmitField('登录 ')



# 找回密码
class FindPasswordForm(Form):
    # 用户名
    username = StringField("用户名")
    # 邮箱
    email = StringField("邮箱")



# 重置密码
class ResetPasswordForm(Form):
    # 密码
    password = PasswordField("密码")
    re_password = PasswordField("密码")


# 修改密码
class ChangePasswordForm(Form):
    # 密码
    old_password = PasswordField()
    password = PasswordField("密码")
    re_password = PasswordField("密码")

# ------------图片验证码生成--------------------------------------------------

# 用来随机生成一个字符串
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

def rndColor():
    ''' 随机颜色'''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def gene_text():
    '''生成4位验证码'''
    return ''.join(random.sample(string.ascii_letters+string.digits, 4))

def draw_lines(draw, num, width, height):
    '''划线'''
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

def get_verify_code():
    '''生成验证码图形'''
    code = gene_text()
    # 图片大小120×50
    width, height = 120, 36
    # 新图片对象
    im = Image.new('RGB',(width, height),'white')
    # 字体
    font = ImageFont.truetype('app/static/Arial.ttf', 40)
    # draw对象
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5+random.randint(-3,3)+23*item, 5+random.randint(-3,3)),
                  text=code[item], fill=rndColor(),font=font )
    # 划线
    draw_lines(draw, 2, width, height)
    # 高斯模糊
    im = im.filter(ImageFilter.GaussianBlur(radius=1.5))
    return im, code
