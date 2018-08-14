from datetime import datetime

from django.db import models
from users.models import UserProfile
from course.models import Course


# Create your models here.

# 用户学习表单
class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'姓名')
    mobile = models.CharField(max_length=11,verbose_name=u'手机')
    course_name = models.CharField(max_length=50,verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户: {0} 手机号: {1}'.format(self.name, self.mobile)


# 用户对于课程评论
class CourseComments(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u'课程')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
    comments= models.CharField(max_length=300,verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'评论时间')

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.course)


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

     class Meta:
         verbose_name = "用户收藏"
         verbose_name_plural = verbose_name

     def __str__(self):
         return '用户({0})收藏了{1} '.format(self.user, self.fav_type)


# 用户消息表
class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u'接收用户')
    message = models.TextField(verbose_name=u'消息内容')
    has_read= models.BooleanField(default=False,verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})接收了{1} '.format(self.user, self.message)

# 用户课程表
class UserCourse(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u'课程')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'用户')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})学习了{1} '.format(self.user, self.course)



