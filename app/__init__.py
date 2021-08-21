from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config, configBD

app = Flask(__name__)
app.config.from_object(configBD)
app.config.from_object(config)
db = SQLAlchemy(app)

from app.main.routes import main
from app.admin.routes import admin



app.register_blueprint(main, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")