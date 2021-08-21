from app import Session, app, Base, engine
from sqlalchemy import Column, String, Integer, Date, DateTime, SmallInteger,Text,Boolean, func, inspect

class Chats(Base):
    __tablename__= 'chats'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)