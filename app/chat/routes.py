from flask_cors import CORS
from app.chat import chat
from flask import render_template

@chat.route('/')
@chat.route('/index')
def index():
        return render_template('chat/chat.html')