from flask_cors import CORS
from app.chat import chat, chat_api
from flask import render_template, jsonify, request
from flask_login import current_user, login_required
from app import Session
from app.chat.models import Chats,ChatMembers,Messages
from app.chat.utils import mserialize_list, dir_serialize_list, enumList
from app.admin.models import User
from datetime import datetime
from sqlalchemy import or_
CORS(chat_api)

@chat.route('/')
@chat.route('/index')
def index():
        Session.close()
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
@login_required
def sendmessage():
    req_data = request.get_json(force=True)
    print(req_data.get('message'), req_data.get('chat_id'))
    message = Messages(message=str(req_data.get('message')), chat_id=int(req_data.get('chat_id')),createtime=datetime.now(),author_id=current_user.id)
    #print(message)
    Session.add(message)
    Session.commit()
    Session.close()
    return jsonify(['Success'])

@chat.route('/getusers')
@chat_api.route('/getusers')
@login_required
def getusers():
    Users = Session.query(User).filter(User.id != current_user.id).all()
    Session.close()
    return jsonify(dir_serialize_list(Users, ['id', 'username']))


@chat_api.route('/createchat', methods=['GET','POST'])
@login_required
def creatchat():
    request_data = request.get_json(force=True)
    text = request_data.get('users')
    print(text)
    usernames = Session.query(User).filter(User.id==text[0]).all()
    title = str(current_user.username + ", "+ usernames[0].username+'...')
    cchat = Chats(title = title)
    Session.add(cchat)
    Session.commit()
    return_id = cchat.id
    members = []
    members.append(ChatMembers(chat_id=cchat.id,member_id=current_user.id))
    for i in range(len(text)):
        members.append(ChatMembers(chat_id=cchat.id,member_id=text[i]))
    Session.add_all(members)
    Session.commit()
    Session.close()
    #parse = text.strip('[]').replace(' ', '').split(',')
    #print(parse)
    return jsonify({'id': return_id}) #вернуть id чата
