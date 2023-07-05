import pymysql
import pymysql
import random
import value

sum = 0


def ViewMessege():
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select * from messegelist "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        conn.rollback()


def Querymember():
    # 打开数据库连接
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    sql = "select ID ,Name,College from teacherlist "
    lis = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for i in results:
            k = list(i)
            k.append("teacher")
            lis.append(k)
    except:
        conn.rollback()

    sql = "select ID ,Name,College from studentlist "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            k = list(i)
            k.append("student")
            lis.append(k)
        conn.close()
        return lis
    except:
        conn.rollback()


def Queryinfomation(res):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()
    k = []
    if res[0] >= '0' and res[0] <= '9':
        res = int(res)
        sql = "select ID ,Name,College,Education,Degree,Identify from teacherlist where ID='%d'" % (res)

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if (len(results) != 0):
                k.append(list(results[0]))
        except:
            conn.rollback()

        sql = "select ID ,Name,College,Major,Identify from studentlist where ID='%d'" % (res)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if (len(results) != 0):
                k.append(list(results[0]))
        except:
            conn.rollback()
        conn.close()

    else:
        sql = "select ID ,Name,College,Education,Degree,Identify from teacherlist where Name LIKE'%%%s%%'" % (res)

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                k.append(list(i))
        except:
            conn.rollback()

        sql = "select ID ,Name,College,Major,Identify from studentlist where Name LIKE'%%%s%%'" % (res)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                k.append(list(i))
            conn.close()
        except:
            conn.rollback()

    return k


def DeleteFomation(idl, idr):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    i = idl
    while (i <= idr):
        sql = "delete  from teacherlist where ID='%d'" % (i)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    i = idl
    while (i <= idr):
        sql = "delete  from studentlist where ID='%d'" % (i)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    i = idl
    while (i <= idr):
        sql = "delete  from account where ID='%d'" % (i)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    conn.close()


def UploadTeacher(lis):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  teacherlist values('%d','%s','%s','%s','%d','%s','%s','%s')" % (
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

        sql = "insert into  account values('%d','%s')" % (i[0], '123456')
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    conn.close()


def UploadStudent(lis):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  studentlist values('%d','%s','%s','%s','%d','%s')" % (i[0], i[1], i[2], i[3], i[4], i[5])
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

        sql = "insert into  account values('%d','%s')" % (i[0], '123456')
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    conn.close()


def UploadCollege(lis):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  collegelist values('%d','%s','%d','%s')" % (i[0], i[1], i[2], i[3])
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    conn.close()


def UploadCourse(res):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    for i in res:
        sql = "insert into  trainingplan values('%d','%s','%d','%s','%d')" % (i[0], i[1], i[2], i[3], i[4])
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    conn.close()


def ArrangeCourse(res):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    # sql = "select  Name,Major from teacherlist "
    teachername = []
    # kkk=[]
    # try:
    #     cursor.execute(sql)
    #     result=cursor.fetchall()
    #     for i in result:
    #         teachername.append(list(i))
    # except:
    #     conn.rollback()
    for i in res:
        sql = "select  Name from teacherlist where Major='%s'" % (i[3])
        kkk = []
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for j in results:
                kkk.append(j[0])
        except:
            conn.rollback()
        teachername.append(kkk)

    # print(teachername)
    sql = " select  * from  classroom "
    Classroom = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            Classroom.append(i[0])
    except:
        conn.rollback()

    temp = [12, 13, 14, 24, 15, 35, 25, 68, 79, 69]
    roomlen = len(Classroom)
    Week = ['周一', '周二', '周三', '周四', '周五']
    cnt = -1
    for i in res:
        global sum
        sum += 1
        cnt += 1

        TN = teachername[cnt][random.randint(0, len(teachername[cnt]) - 1)]

        TP = temp[random.randint(0, 9)]
        CR = Classroom[random.randint(0, roomlen - 1)]
        WK = Week[random.randint(0, 4)]
        sql = "insert  into  course \
        values('%d','%d','%s','%d','%d','%s','%d','%d','%d','%s','%s','%s')" % (sum, i[0], i[1], i[2], TP, \
                                                                                CR, 10, 0, i[4] // 2, i[3], TN, WK)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    conn.close()


# 查培养方案
def ShowTrainProgram(name):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "select * from trainingplan where Major='%s'" % (name)
    try:
        cursor.execute(sql)
        conn.close()
        return cursor.fetchall()
    except:
        conn.rollback()


# 按专业删老师和学生
def delofmajor(name):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "delete  from account where ID in (select ID from studentlist where Major='%s' )" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from account where ID in (select ID from teacherlist where Major='%s' )" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from studentlist where Major='%s'" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from teacherlist where Major='%s' " % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    conn.close()


# 删专业
def DelMAjor(name):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "delete  from collegelist where Major='%s'" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from trainingplan where Major='%s'" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from course where Major='%s'" % (name)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    delofmajor(name)
    conn.close()


# 删除学院
def DelCollege(id):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "delete  from trainingplan where Major in (select  Major from collegelist where CollegeID='%d')" % (id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "delete  from course where Major in (select  Major from collegelist where CollegeID='%d')" % (id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql = "select  Major from collegelist where CollegeID='%d'" % (id)
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for i in res:
            delofmajor(i[0])
    except:
        conn.rollback()

    sql = "delete  from collegelist where CollegeID='%d'" % (id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    conn.close()


def SearchMajor(id):
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "select  Major from collegelist where CollegeID='%d'" % (id)
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except:
        conn.rollback()


def SearchCollege():
    conn = pymysql.connect(host=value.HOST, port=value.PORT, user=value.USER, passwd=value.PASSWD,
                           charset=value.CHARSET, db=value.DB)
    cursor = conn.cursor()

    sql = "select  distinct CollegeID,College from collegelist "
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except:
        conn.rollback()
