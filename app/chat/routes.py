from flask_cors import CORS
from app.chat import chat, chat_api
from flask import render_template, jsonify, request
from flask_login import current_user, login_required
from app import Session
from app.chat.models import Chats,ChatMembers,Messages
from app.chat.utils import mserialize_list, dir_serialize_list, enumList
from app.admin.models import User
from datetime import datetime
CORS(chat_api)

@chat.route('/')
@chat.route('/index')
def index():
        return render_template('chat/chat.html', uid=current_user.id)

@chat.route('/getchats')
@chat_api.route('/getchats')
@login_required
def getchats():
    userchats = [x.chat_id for x in Session.query(ChatMembers.chat_id).filter_by(member_id=current_user.id).distinct()]
    print(userchats)
    chats = Session.query(Chats).filter(Chats.id.in_(userchats)).all()

    Session.close()
    return jsonify(mserialize_list(chats))


@chat.route('/getmessages-<id>')
@chat_api.route('/getmessages-<id>')
@login_required
def getmessages(id):
    #print(datetime.now())
    check = Session.query(ChatMembers).filter_by(chat_id=id, member_id=current_user.id).all()
   # print(check)
    if not check:
        Session.close()
        return jsonify([])
    messages = Session.query(Messages).filter_by(chat_id=id).all()
    users = [[i.id, i.username] for i in Session.query(User).all()]
    for i in range(len(messages)):
        tstatusid = enumList(users, messages[i].author_id)
        messages[i].author_id = users[tstatusid[0]][1]
    Session.close()
    return jsonify(dir_serialize_list(messages,['id','author_id','message','createtime']))

@chat.route('/sendmessage',methods=['POST'])
@chat_api.route('/sendmessage',methods=['POST'])
#@login_required
def sendmessage():
    req_data = request.get_json(force=True)
    print(req_data)
    #message = Messages(req_data.get('message'), req_data.get('chat_id'))
    #Session.add(message)
    #Session.commit()
    Session.close()
    return jsonify(['Success'])

