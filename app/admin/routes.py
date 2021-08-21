from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session
from app import Session
from app.admin.models import User

@admin.route('/')
def index():
        return ""


@admin.route('/login')
def login():
        user = Session.query(User).all()
        return render_template("tableuser.html", user=user)


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
