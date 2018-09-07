from datetime import datetime

from app.database import db


class UserAsk(db.Model):
    """用户学习"""
    __tablename__ = "userask"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),)
    mobile = db.Column(db.String(11))
    course_name = pass
    add_time = db.Column(db.DateTime,default=datetime.now)

class CourseComments(db.Model):
    """ 用户对于课程评论"""
    __tablename__ = "coursecomments"
    id = db.Column(db.Integer,primary_key=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    comments = db.Column(db.String(300))
    add_time = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return '<CourseComments {}>'.format(self.user)


# 用户对于课程，机构，讲师的收藏
class UserFavorite(db.Model):
     __tablename__ = "userfavorite"
     TYPE_CHOICES=(
         (1,u'课程'),
         (2,u'课程机构'),
         (3,u'讲师')
     )
     id = db.Column(db.Integer,primary_key=True)
     user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
     fav_id =db.Column(db.Integer,default=0)
     fav_type = db.Column(db.Integer,default=1)
     add_time = db.Column(db.DateTime,default=datetime.now)

     def __repr__(self):
         return '<UserFavorite {}>'.format(self.user)


# 用户消息表
class UserMessage(db.Model):
    __tablename__ = 'usermessage'
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.Integer,default=0)
    message = db.Column(db.Text)
    has_read = db.Column(db.Boolean,default=False)
    add_time = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return '<UserMessage {}>'.format(self.user)


# 用户课程表
class UserCourse(db.Model):
    __tablename__ = 'usercourse'
    id = db.Column(db.Integer,primary_key=True)

    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u'课程')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
    add_time = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return '<UserCourse {}>'.format(self.user)