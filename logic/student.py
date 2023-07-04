from dataBaseControl.DataStudent import *


class Student:
    time = ["", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]

    def __init__(self, id, name, college, major, grade, identify):
        self.id = id
        self.name = name
        self.college = college
        self.major = major
        self.grade = grade
        self.identify = identify

    def selfinfomation(self):
        """
        返回学生基本信息
        :return: 学号，姓名，学院，专业，年级
        """

        return [self.id, self.name, self.college, self.major, self.grade]

    def selectionresults(self):
        """
        返回学生的选课结果
        :return:选课编号  课程号，课程名，学分，时间（时），地点，老师姓名，时间（天）
                [[1, 2002, '数据结构', 4, '8:00~10:00', '一教101', '老王', '周三']]
        """
        res = electresult(self.id)
        lis = []
        for i in range(len(res)):
            k = list(res[0])
            l = k[4] // 10
            r = k[4] % 10
            k[4] = "%s~%s" % (self.time[l], self.time[r])
            lis.append(k)
        return lis

    def selectplain(self):
        """
        返回学生能选课程
        :return: 每个包括 选课编号 ，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
                [[1, 2002, '数据结构', 4, '8:00~10:00', '一教101', 30, 0, 2, '软件工程', '老王', '周三']]
        """
        # res = Trainplain(self.major, self.grade)
        # lis = []
        # for i in range(len(res)):
        #     k = list(res[0])
        #     k = list(res[i])
        #     l = k[4] // 10
        #     r = k[4] % 10
        #     k[4] = "%s~%s" % (self.time[l], self.time[r])
        #
        # UpDataScore(self.id, selectid, -1)

        res = Trainplain(self.major, self.grade)
        lis = []
        for i in range(len(res)):
            k = list(res[i])
            l = k[4] // 10
            r = k[4] % 10
            k[4] = "%s~%s" % (self.time[l], self.time[r])
            lis.append(k)
        return lis

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

    def choosecourse(self, SelectId, Name, Weektime, Daytime):
        '''

        :param SelectId: 选课编号
        :param Name: 课程名
        :param Weektime: 上课的天 如：周三
        :param daytime: 时间 如13
        :return: 选课成功为true 失败为false
        '''

        if (CheckCourse(Name, self.id) and CheckTime(Weektime, Daytime, self.id) and CheckScore(self.id, SelectId)):
            num = QueryCourse(SelectId)
            if (num[0] >= num[1]):
                AddCourse(self.id, SelectId)
                UpDateCourse(num[1] + 1, SelectId)
                UpDataScore(self.id, SelectId, 1)
                return True
            else:
                return False
        else:
            return False

    # 退课
    def withdrawalcourse(self, selectid):
        '''
        推选课程
        :param selectid: 推选的选课号
        :return:
        '''
        WithdrawalCourse(self.id, selectid)
        UpDataScore(self.id, selectid, -1)


#app = Student(10002, '小沐', '软件与物联网工程学院', '软件工程', 1, 'student')
#print(app.choosecourse(2, 'java', '周三', 12))
app = Student(10001, '杰杰', '软件与物联网工程学院', '软件工程', 2, 'student')
# print(app.choosecourse(2, 'java', '周三', 12))
# # print(app.searchcourse("数据"))
# print(app.withdrawalcourse(2))
for i in app.selectplain():
    print(i)

# app = Student(10002, '小沐', '软件与物联网工程学院', '软件工程', 1, 'student')
# print(app.choosecourse(2, 'java', '周三', 12))
# # print(app.searchcourse("数据"))
# print(app.withdrawalcourse(2))
