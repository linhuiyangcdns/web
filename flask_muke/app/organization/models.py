from app.database import db
from datetime import datetime

class City(db.Model):
    """
    城市
    """
    __tablename__ = 'city'
    name = db.Column(db.String(20))
    desc = db.Column(db.String(200))
    courseorg_id = db.Column(db.Integer, db.ForeignKey('courseorg.id'))
    add_time = db.Column(db.DateTime(),default=datetime.now)

    def __repr__(self):
        return '<City {}>'.format(self.name)



class CourseOrg(db.Model):
    __tablename__ = 'courseOrg'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.Text)
    category = db.Column(db.String(20),default='培训机构')
    tag = db.Column(db.String(10),default='国内名校')
    click_nums = db.Column(db.Integer,default=0)
    fav_nums = db.Column(db.Integer,default=0)
    address = db.Column(db.String(150))
    city = db.relationship('City',backref='user', lazy='dynamic')
    students = db.Column(db.Integer,default=0)
    add_time = db.Column(db.DateTime(),default=datetime.now)
    teachers = db.relationship('Teacher',backref='user',lazy='dynamic')
    courses = db.relationship('Course',backref='courseOrg',lazy='dynamic')

    def __repr__(self):
        return '<City {}>'.format(self.name)



class Teacher(db.Model):
    """
    讲师
    """
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    org_id = db.Column(db.Integer, db.ForeignKey('org.id'))
    name = db.Column(db.String(50))
    work_years = db.Column(db.Integer,default=0)
    work_company = db.Column(db.String(50))
    work_position = db.Column(db.String(50))
    age = db.Column(db.Integer,default=0)
    points = db.Column(db.String(50)) # 教学特点
    click_nums = db.Column(db.Integer,default=0)
    fav_nums = db.Column(db.Integer,default=0)
    courses = db.relationship('Course',backref='teacher',lazy='dynamic')
    add_time = db.Column(db.DateTime(),default=datetime.now)

    def __repr__(self):
        return '<Teacher {}>'.format(self.name)