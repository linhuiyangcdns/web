from datetime import datetime

from app.database import db

from app.organization.models import CourseOrg,Teacher


# 课程信息表
class Course(db.Model):
    """
    用户
    """
    __tablename__ = 'course'
    DEGREE_CHOICES = (
        ('cj',u'初级'),
        ('zj', u'中级'),
        ('gj', u'高级')
    )
    course_org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE, verbose_name=u"所属机构",null=True,blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name=u"讲师", null=True, blank=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True,index=True)
    desc = db.Column(db.String(50)) # 课程描述
    detail = db.Column(db.Text) # 课程详情
    is_banner = db.Column(db.Boolean,default=False) # 是否轮播
    degree = db.Column(db.String(2)) # 程度
    learn_times = db.Column(db.Integer,default=0) # 学习时长（分）
    students = db.Column(db.Integer,default=0) # 学习人数
    fav_nums = db.Column(db.Integer,default=0) # 收藏人数
    image = db.Column(db.Text)  # 图像
    click_nums = db.Column(db.Integer,default=0) # 点击数
    add_time = db.Column(db.DateTime,default=datetime.now) # 添加时间
    category = db.Column(db.String(20),default='后端开发') # 课程类别
    tag = db.Column(db.String(15),default='') # 课程标签




# 章节
class Lesson(db.Model):
    course =
    name = db.Column(db.String(100))
    add_time = db.Column(db.DateTime,default=datetime.now)

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course,self.name)


# 视频
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}章节的视频 >> {1}'.format(self.lesson,self.name)


# 课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    download = models.FileField(
        upload_to = 'course/resource/%Y/%m',
        verbose_name=u'资源文件',
        max_length=100
    )

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的资源: {1}'.format(self.course,self.name)
