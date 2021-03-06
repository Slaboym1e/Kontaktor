from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session
from app import Session
from app.admin.models import User, Area, residents, staff
from flask_login import current_user, login_user, logout_user, login_required
from app.admin.WTForms import LoginForm, CreateResidentForm, CreateAreatForm
from app.admin.utils import createListUsers, createListAreas
from app.chat.utils import enumList
import app.main
from array import *

@admin.route('/')
def index():
        if current_user.is_authenticated:
            Session.close()
            return render_template('admin/index.html')
        Session.close()
        return redirect(url_for('main.index'))

@admin.route('/videocampage')
def videocampage():
    if current_user.is_authenticated:
        Session.close()
        return render_template('admin/videocam.html')
    Session.close()
    return redirect(url_for('main.index'))

@admin.route('/buhgalter')
def buhgalter():
    if current_user.is_authenticated:
        Session.close()
        return render_template('admin/buhgalter.html')
    Session.close()
    return redirect(url_for('main.index'))



@admin.route('/area')
def area():
    areas = Session.query(Area).all()
    for area in areas:
        area.square = round(float(area.height) * float(area.width), 2)
    Session.close()
    return render_template('admin/docs.html', areas=areas)

@admin.route('/residents')
def residentsview():
    resident = Session.query(residents).all()
    users = [[i.id, i.username] for i in Session.query(User).filter_by(group_id=2).all()]
    for i in range(len(resident)):
        dirs = enumList(users, resident[i].director_id)
        resident[i].director_id = users[dirs[0]][1]
    Session.close()
        #print(resident[i].director_id)
    return render_template('admin/residents.html', residents=resident)

@admin.route('/residentcreate', methods=['GET', 'POST'])
def rescreate():
    form = CreateResidentForm()
    form.dirid.choices = createListUsers(2)
    form.areaid.choices = createListAreas()
    if form.validate_on_submit():
        if form.dirid.data !="" and form.areaid.data != "":
            res = residents(resname=form.resname.data, director_id=form.dirid.data)
            Session.add(res)
            Session.commit()
            Session.add(staff(resident_id=res.id, user_id=res.director_id))
            area = Session.query(Area).filter_by(id=form.areaid.data).first()
            area.user_id = res.id
            Session.commit()
            Session.close()
            return redirect(url_for('admin.residentsview'))
    Session.close()
    return render_template('admin/rescreate.html', form=form)

@admin.route('/areacreate', methods=['GET', 'POST'])
def areacreate():
    form = CreateAreatForm()
    if form.validate_on_submit():
        Session.add(Area(title=form.arname.data,height=form.heigth.data,width=form.width.data, user_id=0))
        Session.commit()
        Session.close()
        return redirect(url_for('admin.area'))
    Session.close()
    return render_template('admin/areacreate.html', form=form)
# @admin.route('/areaa')
# def areaa():
#     area = Area(title='????????????????', width='140', height='200', user_id='1')
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
