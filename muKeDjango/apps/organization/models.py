from datetime import datetime

from django.db import models


#城市字典
class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'城市')
    desc = models.CharField(max_length=200,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#课程机构
class CourseOrg(models.Model):
    ORG_CHOICES =(
        ('pxjg',u"培训机构"),
        ("gx","高校"),
        ("gr",u"个人")
    )
    name = models.CharField(max_length=50,verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏数')
    image = models.ImageField(
        upload_to='org/%Y/%m',
        verbose_name=u'封面图',
        max_length=100
    )
    address = models.CharField(max_length=150,verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name=u'所在城市')
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name=u"机构类别", default="pxjg")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    tag = models.CharField(max_length=20,default=u'国内名校',verbose_name=u'机构标签')

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '课程机构：{0}'.format(self.name)

# 讲师
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name=u'所属机构')
    name= models.CharField(max_length=50,verbose_name=u'教师名称')
    work_years= models.IntegerField(default=0,verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50,verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50,verbose_name=u'公司职位')
    points = models.CharField(max_length=50,verbose_name=u'教学特点')
    click_nums= models.IntegerField(default=0,verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏数')
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name=u"头像",
        max_length=100)


    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)