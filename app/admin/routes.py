from app.admin import admin
from flask import render_template, request, flash, redirect, url_for, session

@admin.route('/')
def index():
        return ""


@admin.route('/login')
def login():
        return render_template("tableuser.html")


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
