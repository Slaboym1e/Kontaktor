from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
        return "Hello, world!!!"


@main.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404
