import pymysql
import random
from faker import Faker


# 查帐号
def quiryaccount(id,password):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',charset='utf8',db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql="select ID from account where ID='%d' and Password='%s' " %(id,password)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if (len(results)==0):
            return [False,0,'wrong']
        else:
            if(id==10001):
                conn.close()
                return [True, id,'admin']
            elif(id>2000):
                conn.close()
                return [True, id,'student']
            else:
                conn.close()
                return [True, id, 'teacher']

    except:
        conn.rollback()

#查询学生信息
def QuiryStudent(id):
    '''
    查询学生信息
    :param id:
    :return:
    '''
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select * from studentlist where ID='%d' " % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    except:
        conn.rollback()

# 查选课结果
def electresult(id):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select SelectID,CourseID,CourseName,score,CourseTime,CoursePlace,TeacherName from course where SelectID in\
    (select selectresult.SelectID from selectresult where ID='%d') " % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results
    except:
        conn.rollback()

# 查找能选课程
def Trainplain(major,grade):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql="select * from course where major='%s' and grade='%d' " % \
        (major,grade)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results

    except:
        conn.rollback()

# 按名字查找课程
def SearchCourse(coursename):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select CourseID,CourseName,score,CourseTime,CoursePlace,Num,Selectnum from course where CourseName like '%%%s%%'" %(coursename)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results

    except:
        conn.rollback()

#查询课程
def QueryCourse(id):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select Num from course where SelectID = '%d'" % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        k=results[0][0]
        return k

    except:
        conn.rollback()


#添加选课
def AddCourse(id,selectid):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "insert into   selectresult values('%d','%d')" % (id,selectid)

    try:
        cursor.execute(sql)
        conn.commit()
        conn.close()

    except:
        conn.rollback()

#是否已选择课程
def CheckCourse(name):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select * from (selectresult,course)  where CourseName = '%s'" % (name)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        if(len(results)==0):
            return False
        else:
            return True
    except:
        conn.rollback()


#修改课程信息
def UpDateCourse(num,selectid):
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "UPDATE employees  SET Num = '%d' WHERE \
    SelectID = '%d' " % (num, selectid)

    try:
        cursor.execute(sql)
        conn.commit()
        conn.close()

    except:
        conn.rollback()
















