from app import Session
from app.admin.models import User,Area

def createListUsers(id):
    w = Session.query(User).filter(User.group_id == id).all()
    #w = User.query.filter(User.group_id==id).options(load_only("id", "surname", "name", "secondname")).all()
    if(len(w)>0):
        list = [("", 'Не выбрано')]
        #list =[]
        for i in w:
            list.append((i.id, i.username))
    else:
        list = [("", 'Not available')]
    return list

def createListAreas():
    w = Session.query(Area).filter(Area.user_id == 0).all()
    #w = User.query.filter(User.group_id==id).options(load_only("id", "surname", "name", "secondname")).all()
    if(len(w)>0):
        list = [("", 'Не выбрано')]
        #list =[]
        for i in w:
            list.append((i.id, i.title+' Площадь: '+str(i.height*i.width)+' кв.м'))
    else:
        list = [("", 'Нет доступных помещений')]
    return list