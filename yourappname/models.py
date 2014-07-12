# code from http://flask.pocoo.org/docs/patterns/sqlalchemy/

from sqlalchemy import Column, Integer, String
from . import db
from yourappname.database import Base

# from https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html#a-minimal-application
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# see https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html for inserting records
