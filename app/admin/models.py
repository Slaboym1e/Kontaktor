from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, Date, SmallInteger
from app import Base



class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username   = Column(String(64), unique=True, nullable=False)
    group_id   = Column(String(12), unique=False, nullable=True, default='user')


def __init__(self, username=None, group_id=None):
    self.username = username
    self.group_id = group_id


def __repr__(self):
    return '<User %r>' % self.username
