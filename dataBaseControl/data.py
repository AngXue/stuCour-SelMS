import pymysql
import random
from faker import Faker

# 打开数据库连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123456',
                       charset='utf8',
                       db="test"
                       )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#查帐号
def quiryaccount(id,password):

    sql="select ID from account where ID='%d' and Password='123456' " %(id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if (len(results)==0):
            return [False,0,'wrong']
        else:
            if(id==10001):
                return [True, id,'admin']
            elif(id>2000):
                return [True, id,'student']
            else:
                return [True, id, 'teacher']

    except:
        conn.rollback()

#查选课结果
def electresult(id):

    sql = "select CourseID,CourseName,score,CourseTime,CoursePlace from course where SelectID=\
    (select selectresult.SelectID from selectresult where ID='%d') " % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        return results
    except:
        conn.rollback()

#查找能选课程
def Trainplain(major,grade):

    sql="select CourseID,CourseName,score,CourseTime,CoursePlace,Num,Selectnum from course where major='%s' and grade='%d' " % \
        (major,grade)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    except:
        conn.rollback()


