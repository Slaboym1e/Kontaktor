from flask import Blueprint

chat = Blueprint('chat', __name__)
chat_api = Blueprint('chat_api',__name__)

import app.chat.routes
