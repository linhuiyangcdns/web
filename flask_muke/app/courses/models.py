from datetime import datetime

from app.database import db

from app.organization.models import CourseOrg,Teacher


# 课程信息表
class Course(db.Model):
    """
    用户
    """
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))
    course_org_id = db.Column(db.Integer,db.ForeignKey('courseOrg.id'))
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

    def __repr__(self):
        return '<Course {}>'.format(self.name)



# 章节
class Lesson(db.Model):
    __tablename__ = "lesson"
    id = db.Column(db.Integer,primary_key=True)
    course =
    name = db.Column(db.String(100))
    add_time = db.Column(db.DateTime,default=datetime.now)



    def __repr__(self):
        return '<Lesson {}>'.format(self.name)


# 视频
class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer,primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    url = db.Column(db.String(200),default="")
    name = db.Column(db.String(100),default="视频名")
    learn_times = db.Column(db.Integer,default=0)
    add_time = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return '<Video {0}>'.format(self.name)




# 课程资源
class CourseResource(db.Model):
    __tablename__ = "courseresource"
    id = db.Column(db.Integer,primary_key=True)
    course = models.ForeignKey(Course, verbose_name=u'课程',on_delete=models.CASCADE)
    name = db.Column(db.String(100))
    add_time = db.Column(db.DateTime,default=datetime.now)

    download = models.FileField(
        upload_to = 'course/resource/%Y/%m',
        verbose_name=u'资源文件',
        max_length=100
    )

    def __repr__(self):
        return '<CourseResource {0}>'.format(self.name)
