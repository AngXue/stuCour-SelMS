import pymysql
import random
from faker import Faker
import value


# 查帐号
def quiryaccount(id,password):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql="select ID from account where ID='%d' and Password='%s' " %(id,password)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if (len(results)==0):
            return [False,0,'wrong']
        else:
            if(id==123456):
                conn.close()
                return [True, id,'admin']
            elif(id>10000):
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
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
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
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select SelectID,CourseID,CourseName,score,CourseTime,CoursePlace,TeacherName,Time from course where SelectID in\
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
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
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
def SearchCourse(res):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    k = []
    if res[0] >= '0' and res[0] <= '9':
        res = int(res)
        sql = "select * from course where CourseId = '%s'" %(res)

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                k.append(i)
            conn.close()
        except:
            conn.rollback()
    else:
        sql = "select * from course where CourseName LIKE'%%%s%%'" % (res)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                k.append(i)
        except:
            conn.rollback()

    return k
#查询课程
def QueryCourse(id):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select Num,Selectnum from course where SelectID = '%d'" % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        k=[]
        k.append(results[0][0])
        k.append(results[0][1])
        return k

    except:
        conn.rollback()


#添加选课
def AddCourse(id,selectid):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
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
def CheckCourse(name,id):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select course.CourseName from selectresult,course  where selectresult.SelectID = course.SelectID and selectresult.ID='%d'" %(id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        for i in results:
            if(name==i[0]):
                return False
        return True
    except:
        conn.rollback()


#修改课程信息
def UpDateCourse(num,selectid):
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "UPDATE course  SET Selectnum = '%d' WHERE \
    SelectID = '%d' " % (num, selectid)

    try:
        cursor.execute(sql)
        conn.commit()
        conn.close()

    except:
        conn.rollback()


def CheckTime(weektime,daytime,id):
    '''
    检查学生时间是否冲突
    :param weektime: 周三
    :param daytime:  13
    :param id:  选课人学号
    :return: 不冲突 true, 冲突为false
    '''
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # sql = "select course.CourseName from selectresult,course  where selectresult.SelectID = course.SelectID \
    # and selectresult.ID='%d'" % (
    #     id)
    sql = "select Time,CourseTime from selectresult,course  where selectresult.SelectID = course.SelectID\
            and ID='%d' " % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        for i in results:
            if(weektime==i[0] and check(daytime,i[1])):
                return False
        return True
    except:
        conn.rollback()

def check(a,b):
    lisa=[]
    lisb=[]
    l=a//10
    r=a%10
    while(l<=r):
        lisa.append(l)
        l+=1
    l = b // 10
    r = b % 10
    while (l <= r):
        lisb.append(l)
        l += 1
    for i in lisa:
        for j in lisb:
            if(i==j):
                return True

    return False


def CheckScore(id,selectid):
    '''
    检查学分是否还够
    :param id:
    :param selectid:
    :return:  够 true 不够 false
    '''
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select * from course where SelectID = '%d'  " % (selectid)
    score1=0
    score2=0
    sum = 0
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        score1+=results[0][3]
    except:
        conn.rollback()

    sql = "select * from studentscore where ID = '%d'  " % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        sum+=results[0][1]
        score2+=results[0][2]
    except:
        conn.rollback()

    if(sum>=score1+score2):
        sql = "UPDATE studentscore  SET score = '%d' WHERE ID = '%d' " % (score1, score2)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return True
    else:
        return False


#撤销课程
def WithdrawalCourse(id,selectID):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "DELETE FROM selectresult WHERE SelectID='%d' and ID='%d' " % (selectID,id)

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "select Selectnum from course where SelectID = '%d'  " % (selectID)
    num=0
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        num = results[0][0]
    except:
        conn.rollback()

    sql = "UPDATE course  SET Selectnum = '%d' WHERE SelectID = '%d' " % (num-1, selectID)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    conn.close()

#跟新学分
def UpDataScore(id,selectid,flag):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD, charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select score from course where SelectID = '%d'  " % (selectid)
    score1 = 0
    score2 = 0
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        score1 += results[0][0]
    except:
        conn.rollback()

    sql = "select score from studentscore where ID = '%d'  " % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        score2 += results[0][0]
    except:
        conn.rollback()



    sql = "UPDATE studentscore  SET score = '%d' WHERE ID = '%d' " % (score2 + flag*score1, id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    conn.close()



def GetScore(id):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select score from studentscore where ID = '%d'  " % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results[0][0]
    except:
        conn.rollback()
















