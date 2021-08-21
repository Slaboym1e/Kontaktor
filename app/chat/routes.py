from flask_cors import CORS
from app.chat import chat, chat_api
from flask import render_template, jsonify
from flask_login import current_user
from app import Session
from app.chat.models import Chats,ChatMembers
from app.chat.utils import mserialize_list


@chat.route('/')
@chat.route('/index')
def index():
        return render_template('chat/chat.html')

#@chat.route('/getchats')
#@chat_api.route('/getchats')
#def getchats():
    #userchats = [x.id for x in Session.query(ChatMembers.id).filter_by(member_id=current_user.id).distinct()]
    #chats = Session.query(Chats).filter(Chats.id.in_(userchats)).all()
    #Session.close()
    #return jsonify(mserialize_list(chats))

