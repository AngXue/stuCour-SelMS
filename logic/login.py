from dataBaseControl.DataStudent import *
from dataBaseControl.DataTeacher import *
import student as st
import teacher as te
import admin as ad

def login(id, password):
    """
    :param id: 学号或工号
    :param password: 密码
    :return:  list 账户存在则为[True,id],否则为[Flase,0]
    """
    return quiryaccount(id, password)

def createobject(id,identify):
    '''
    实例化对象
    :param id: 学号或工号
    :param identify: 身份
    :return: 老师或学生或管理员
    '''
    if(identify=='student'):
        res=QuiryStudent(id)
        t=list(res[0])
        return st.Student(t[0],t[1],t[2],t[3],t[4],t[5])
    elif(identify=='teacher'):
        res = QuiryTeacher(id)
        t=list(res[0])
        return te.Teacher(t[0], t[1], t[2], t[3], t[4], t[5],t[6])
    else:
        return ad.Admin()

# app=createobject(1,'admin')
# print(app.viewmessage())