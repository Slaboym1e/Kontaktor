from flask import Blueprint

chat = Blueprint('chat', __name__)

import app.chat.routes
