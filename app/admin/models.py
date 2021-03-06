from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, Date, SmallInteger, Float
from app import Base, engine,Session



class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    group_id = Column(String(12), unique=False, nullable=True, default='user')



    def __init__(self, username=None, group_id=None):
        self.username = username
        self.group_id = group_id


    def __repr__(self):
        return '<User %r>' % self.username


# @login.user_loader
# def load_user(user_id):
#     return User.get(user_id)

@login.user_loader
def load_user(id):
    #return User.id(id)
    return Session.query(User).filter(User.id == id).first()

class residents(Base):
    __tablename__='Residents'
    id=Column(Integer, primary_key=True, autoincrement=True)
    resname=Column(String(255), nullable=True)
    director_id = Column(Integer, nullable=False)

class staff(Base):
    __tablename__='resident_staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resident_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class Area(UserMixin, Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title   = Column(String(64), unique=False, nullable=False)
    height   = Column(Float(12), unique=False, nullable=False)
    width = Column(Float(12), unique=False, nullable=False)
    user_id = Column(Integer, nullable=True)




Base.metadata.create_all(bind=engine)
