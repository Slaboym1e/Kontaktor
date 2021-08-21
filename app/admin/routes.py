from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session
from app import Session
from app.admin.models import User
from flask_login import current_user, login_user, logout_user, login_required
import app.main

@admin.route('/')
def index():
        if current_user.is_authenticated:
                return redirect(url_for('main.index'))
        return ""


@admin.route('/login')
def login():
        user = Session.query(User).all()
        Session.close()
        return render_template("admin/tableuser.html", user=user)


@admin.route('/authorize/<int:id>')
def authorize(id):
        user = Session.query(User).filter_by(id=id).first()
        login_user(user)
        Session.close()
        return redirect(url_for('main.index'))

@admin.route('/logout')
def logout():
    Session.close()
    logout_user()
    return redirect(url_for('admin.login'))

# @admin.route('/registre', methods=['GET', 'POST'])
# def reg():
#     user = User(username = "admin", group_id="admin")
#     Session.add(user)
#     Session.commit()
#     Session.close()
#     user = Session.query(User).all()
#     return render_template("admin/tableuser.html", user=user)


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
