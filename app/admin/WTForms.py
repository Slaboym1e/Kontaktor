from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators

class LoginForm(FlaskForm):
    username = StringField('')
    submit = SubmitField('Войти')