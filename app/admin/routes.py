from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session
from app import Session
from app.admin.models import User, Area, residents, staff
from flask_login import current_user, login_user, logout_user, login_required
from app.admin.WTForms import LoginForm, CreateResidentForm
from app.admin.utils import createListUsers
import app.main
from array import *

@admin.route('/')
def index():
        if current_user.is_authenticated:
            return render_template('admin/index.html')
        return redirect(url_for('main.index'))

@admin.route('/area')
def area():
    areas = Session.query(Area).all()
    for area in areas:
        area.square = round(float(area.height) * float(area.width), 2)
    Session.close()
    return render_template('admin/docs.html', areas=areas)

@admin.route('/residents')
def residents():
    return render_template('admin/residents.html')


@admin.route('/more/<int:id>')
def more(id):
    area = Session.query(Area).filter_by(id=id).first()
    square = round(float(area.height) * float(area.width), 2)
    user = Session.query(User).filter_by(id=area.user_id).first()
    Session.close()
    return render_template('admin/more.html', square=square, area=area, user=user)


@admin.route('/residentcreate', methods=['GET', 'POST'])
def rescreate():
    form = CreateResidentForm()
    form.dirid.choices = createListUsers(2)
    if form.validate_on_submit():
        if form.dirid.data !="":
            res = residents(resname=form.resname.data, director_id=form.dirid.data)
            Session.add(res)
            Session.commit()
            Session.close()
            redirect(url_for('admin.rescreate'))
    Session.close()
    return render_template('admin/rescreate.html', form=form)


# @admin.route('/areaa')
# def areaa():
#     area = Area(title='Помидоры', width='140', height='200', user_id='1')
#     Session.add(area)
#     Session.commit()
#     Session.close()
#     return "11"


@admin.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form=LoginForm()
    user = Session.query(User).all()
    select = request.form.get('comp_select')
    Session.close()
    return render_template("admin/tableuser.html", user=user, select=select, form=form)

@admin.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select))


@admin.route('/authorize', methods=['GET', 'POST'])
def authorize():
        select = request.form.get('comp_select')
        user = Session.query(User).filter_by(username=select).first()
        login_user(user)
        Session.close()
        return redirect(url_for('main.index'))

@admin.route('/logout')
def logout():
    Session.close()
    logout_user()
    return redirect(url_for('admin.login'))

@admin.route('/registre', methods=['GET', 'POST'])
def reg():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get('new_user')
        user = User(username = username, group_id=2)
        Session.add(user)
        Session.commit()
        Session.close()
        user = Session.query(User).all()
        return redirect(url_for('admin.login'))
    return render_template("admin/registre.html", form=form)


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
