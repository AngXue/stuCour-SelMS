from dataBaseControl.DataAdmin import *
import pandas as pd


class Admin:
    def __init__(self):
        self.flag = False

    def viewmessage(self):
        return ViewMessege()

    def allinfomation(self):
        '''
        显示老师和学生的信息
        :return:[ID，名字，所属学院，身份]
                [[1001, '老王', '艺术学院', 'teacher'], [50001, '陈名杰', '软件与物联网工程', 'student']]
        '''
        return Querymember()

    def queryinfomation(self, res):
        '''
        根据学号或姓名查找用户
        :param res: 学号或姓名 Sting类型
        :return: [[1001, '老杰', '艺术学院', '硕士研究生', '博士学位', 'teacher'], [50001, '陈名杰', '软件与物联网工程', '软件工程', 'student']]
        '''
        return Queryinfomation(res)

    def deletefomatin(self, idl, idr):
        '''
        删除idl到idr区间的所有用户
        :param idl: int型
        :param idr: int型
        :return:
        '''
        DeleteFomation(idl, idr)

    def uploadteacher(self, place):
        '''
        将excel文件读入老师信息
        :param place: 文件绝对路径
        :return:
        '''
        df = pd.read_excel(place)

        res = []
        for i in range(df.shape[0]):
            lis = []
            for j in df.values[i]:
                lis.append(j)
            res.append(lis)
        UploadTeacher(res)

    def uploadstudent(self, place):
        '''
        将excel文件读入学生信息
        :param place: 文件绝对路径
        :return:
        '''

        df = pd.read_excel(place)
        res = []
        for i in range(df.shape[0]):
            lis = []
            for j in df.values[i]:
                lis.append(j)
            res.append(lis)
        UploadStudent(res)

    def uploadcollege(self, place):
        '''
        上传学院和专业信息
        :param place: 绝对路径
        :return:
        '''
        df = pd.read_excel(place)
        res = []
        for i in range(df.shape[0]):
            lis = []
            for j in df.values[i]:
                lis.append(j)
            res.append(lis)
        UploadCollege(res)

    def opencourse(self):
        '''
        开启选课
        :return:
        '''
        self.flag = True

    def closecourse(self):
        '''
        关闭选课
        :return:
        '''
        self.flag = False

    def getcourse(self):
        '''
        是否已开启选课
        :return: bool变量
        '''
        return self.flag

#
# app = Admin()
# print(app.uploadstudent("Student.xlsx"))
#print(app.uploadteacher("Teacher.xlsx"))
