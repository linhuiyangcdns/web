from datetime import datetime

from app.database import db

from app.organization.models import CourseOrg,Teacher


# 课程信息表
class Course(models.Model):
    DEGREE_CHOICES = (
        ('cj',u'初级'),
        ('zj', u'中级'),
        ('gj', u'高级')
    )
    course_org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE, verbose_name=u"所属机构",null=True,blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name=u"讲师", null=True, blank=True)
    name = models.CharField(max_length=50,verbose_name=u'课程名')
    desc = models.CharField(max_length=50,verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    degree = models.CharField(max_length=2,choices=DEGREE_CHOICES)
    learn_times = models.IntegerField(default=0,verbose_name=u'学习时长（分）')
    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')

    image = models.ImageField(
        upload_to='course/%Y/%m',
        verbose_name=u'封面图',
        max_length=100
    )
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    category = models.CharField(max_length=20, verbose_name=u"课程类别", default=u"后端开发")
    tag = models.CharField(max_length=15, verbose_name=u"课程标签", default=u"")

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节
class Lesson(models.Model):
    # on_delete=models.CASCADE级联删除
    course= models.ForeignKey(Course,verbose_name=u'课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

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
