from flask import Blueprint, render_template

admin = Blueprint('main', __name__)


@admin.route('/')
def index():
        return "Hello, world!!!"


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
