from app import Session, app, Base, engine
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Text
from flask_login import current_user
from datetime import datetime


class Chats(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), unique=False, nullable=False)


class ChatMembers(Base):
    __tablename__ = 'chat_members'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, nullable=False)
    member_id = Column(Integer, nullable=False)


class Messages(Base):
    __tablename__ = 'chat_messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    createtime = Column(DateTime)
    message = Column(Text)

    # def __init__(self, message, chat_id):
    #     self.author_id = current_user.id
    #     self.message = message
    #     self.createtime = datetime.now()
    #     self.chat_id = chat_id


class AdditionFiles(Base):
    __tablename__ = 'chat_addfiles'
    id = Column(Integer, primary_key=True , autoincrement=True)
    message_id = Column(BigInteger, nullable=False)
    filename = Column(String(255), nullable=False)


Base.metadata.create_all(bind=engine)
