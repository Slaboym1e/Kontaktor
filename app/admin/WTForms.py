from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, SelectField, FloatField

class LoginForm(FlaskForm):
    username = StringField('')
    submit = SubmitField('Войти')

class CreateResidentForm(FlaskForm):
    resname = StringField('Название Резидента')
    dirid = SelectField('Выбор главы', default=0)
    areaid = SelectField('Выбор свободного помещения', default=0)
    subbutton = SubmitField('Создать')

class CreateAreatForm(FlaskForm):
    arname = StringField('Название Помещения')
    heigth = FloatField('Длина помешения')
    width = FloatField('Ширина помещения')
    subbutton = SubmitField('Добавить помещение')