from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
        return "Hi"


@admin.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
