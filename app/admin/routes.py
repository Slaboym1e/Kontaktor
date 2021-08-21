from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session
from app import Session
from app.admin.models import User
from flask_login import current_user, login_user, logout_user, login_required
from app.admin.WTForms import LoginForm
import app.main

@admin.route('/')
def index():
        if current_user.is_authenticated:
                return redirect(url_for('main.index'))
        return ""


@admin.route('/login')
def login():
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
    user = User(username = "buhgalet", group_id="user")
    Session.add(user)
    Session.commit()
    Session.close()
    user = Session.query(User).all()
    return 140


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
