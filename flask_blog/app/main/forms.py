from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Length,DataRequired

from ..models import User,Role


class EditProfileForm(FlaskForm):
    name = StringField('昵称', validators=[DataRequired(),Length(0, 64)])
    location = StringField('所在地', validators=[DataRequired,Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')


class PostForm(FlaskForm):
    titile = StringField('提交你的标题',validators=[DataRequired()])
    body = TextAreaField('你的文章内容',validators=[DataRequired()])
    submit = SubmitField('提交')

class CommentForm(FlaskForm):
    body = TextAreaField('你的评论内容')
    submit = SubmitField('提交')