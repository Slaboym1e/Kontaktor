import os
basedir = os.path.abspath(os.path.dirname(__file__))

class configBD_local(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('//216.216.216.1/database', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class configBD(object):
    SQLALCHEMY_DIALECT  = 'mysql'
    SQLALCHEMY_DRIVER   = 'pymysql'
    SQLALCHEMY_USER     = 'a0529774_kontaktor'
    SQLALCHEMY_PASSWORD = 'Tpk3b2Hf'
    SQLALCHEMY_HOST     = '141.8.192.26'
    SQLALCHEMY_DBNAME   = 'a0529774_kontaktor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DIALECT+'+'+SQLALCHEMY_DRIVER+'://'+\
                              SQLALCHEMY_USER+':'+SQLALCHEMY_PASSWORD+'@'+\
                              SQLALCHEMY_HOST+'/'+SQLALCHEMY_DBNAME

class config(object):
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    DEBUG = True
    TESTING = False
    SECRET_KEY = '2a62cf81dc7b6243a57516f447a84ba627bba87384e7ee614bb93a3ada7be69f'


