from dataBaseControl.DataAdmin import *
import pandas as pd


class Admin:
    time = ["", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
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
        # 读取excel文件
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


    #上传课程或培养方案
    def uploadcourse(self,place):
        '''
        上传课程
        :param
        place: 文件地址
        :return:
        '''
        df = pd.read_excel(place)
        #print(df)
        res = []
        for i in range(df.shape[0]):
            lis = []
            for j in df.values[i]:
                lis.append(j)
            res.append(lis)
        #print(res)

        UploadCourse(res)
        ArrangeCourse(res)

    def showTrainProgram(self,collegeid,majorname):
        return ShowTrainProgram(majorname)

    def delMajor(self,collegeid,majorname):
        DelMAjor(majorname)

    def delCollege(self,collegeid):
        DelCollege(collegeid)

    def searchmajor(self,collegeid):
        '''
        获取学院的专业
        :param collegeid:
        :return:
        '''
        return SearchMajor(collegeid)

    def searchcollege(self):
        return SearchCollege()

    def searchcourse(self, coursename):
        """
        :param coursename: 搜索的课程名，不需要全名
        :return: 每个包括 选课编号 ，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
                [[1, 2002, '数据结构', '~11:00', 13, '一教101', 30, 0, 2, '软件工程', '老王', '周三']]
        """
        res = SearchCourse(coursename)
        lis = []
        for i in range(len(res)):
            k = list(res[i])
            l = k[4] // 10
            r = k[4] % 10
            k[4] = "%s~%s" % (self.time[l], self.time[r])
            lis.append(k)
        return lis

# app = Admin()
# print(app.uploadstudent("Student.xlsx"))
# print(app.uploadcourse(r'F:\stuCour-SelMS\logic\data\软件工程.xlsx'))
# print(app.uploadteacher("Teacher.xlsx"))
# print(app.delMajor(1,'软件工程'))
# print(app.delCollege(1))
#app.uploadcollege("College.xlsx")

# app.delCollege(101)


