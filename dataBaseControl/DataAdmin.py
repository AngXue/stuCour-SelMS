import pymysql


def Querymember():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
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

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
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


def DeleteFomation(idl,idr):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    i=idl
    while(i<=idr):
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
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  teacherlist values('%d','%s','%s','%s','%d','%s','%s')" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6])
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
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  studentlist values('%d','%s','%s','%s','%d','%s')" % (i[0], i[1], i[2], i[3], i[4],i[5])
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
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', charset='utf8', db="test")
    cursor = conn.cursor()

    for i in lis:
        sql = "insert into  collegelist values('%d','%s','%d','%s')" % (i[0], i[1], i[2], i[3])
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    conn.close()
