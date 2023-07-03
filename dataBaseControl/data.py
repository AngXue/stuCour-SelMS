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


def quiryaccount(id,password):

    sql="select ID from account where ID='%d' and Password='123456' " %(id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if (len(results)==0):
            return (False,0)
        else:
            return (True,id)
    except:
        conn.rollback()


def electresult(id):
    sql = "select * from selectresult where ID='%d' " % (id)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        return results
    except:
        conn.rollback()
