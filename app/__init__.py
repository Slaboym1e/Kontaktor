from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from app.config import config, configBD
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object(configBD)
app.config.from_object(config)
#db = SQLAlchemy(app)
engine = create_engine(configBD.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
Session =scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

from app.main.routes import main
from app.admin.routes import admin
from app.chat.routes import chat



app.register_blueprint(main, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(chat, url_prefix="/chat")