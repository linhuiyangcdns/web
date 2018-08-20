from flask import render_template,abort,redirect,flash,url_for
from flask_login import login_required,current_user

from . import operation
from app import db
from datetime import datetime


@operation.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')