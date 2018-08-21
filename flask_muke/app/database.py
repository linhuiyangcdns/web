from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()
