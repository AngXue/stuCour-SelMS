import pymysql
import random
from faker import Faker

#发送老师信息
def feedbackmessege(name,s):
    '''
    发送信息给管理员
    :param name:
    :param s:
    :return:
    '''
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    sql="insert into messegelist (Name,Messege) values('%s','%s') " %(name,s)

    try:
        cursor.execute(sql)
        conn.commit()

    except:
        conn.rollback()

    conn.close()

#查看任课表
def SearchTeaching(name):
    '''
    查看课表
    :param name:
    :return: 课表
    '''

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    sql = "select CourseID,CourseName,score,CourseTime,CoursePlace,Selectnum from course where TeacherName='%s' " % (name)

    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        return result

    except:
        conn.rollback()

    conn.close()

def QuiryTeacher(id):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    sql = "select * from teacherlist where ID='%d' " % (id)

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except:
        conn.rollback()

    conn.close()