from datetime import datetime

from app.database import db


class UserAsk(db.Model):
    """用户学习"""
    name = db.Column(db.String(20),)
    mobile = db.Column(db.String(11))
    course_name = pass
    add_time = db.Column(db.DateTime,default=datetime.now)

class CourseComments(db.Model):
    """ 用户对于课程评论"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    comments = models.CharField(max_length=300, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'评论时间')

# 用户对于课程，机构，讲师的收藏
class UserFavorite(models.Model):
     TYPE_CHOICES=(
         (1,u'课程'),
         (2,u'课程机构'),
         (3,u'讲师')
     )
     user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
     fav_id = models.IntegerField(default=0)
     fav_type = models.IntegerField(
         choices=TYPE_CHOICES,
         default=1,
         verbose_name=u'收藏类型'
     )
     add_time = models.DateTimeField(default=datetime.now,verbose_name=u'评论时间')

# 用户消息表
class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u'接收用户')
    message = models.TextField(verbose_name=u'消息内容')
    has_read= models.BooleanField(default=False,verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


# 用户课程表
class UserCourse(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u'课程')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')