import os
basedir = os.path.abspath(os.path.dirname(__file__))

class configBD(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class config(object):
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    DEBUG = True
    TESTING = False
    SECRET_KEY = '2a62cf81dc7b6243a57516f447a84ba627bba87384e7ee614bb93a3ada7be69f'


