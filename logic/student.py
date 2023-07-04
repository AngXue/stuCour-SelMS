from dataBaseControl.DataStudent import *


class Student:
    time = ["", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]

    def __init__(self, id, name, college, major, grade):
        self.id = id
        self.name = name
        self.college = college
        self.major = major
        self.grade = grade

    def selfinfomation(self):
        """
        返回学生基本信息
        :return: 学号，姓名，学院，专业，年级
        """

        return [self.id, self.name, self.college, self.major, self.grade]

    def selectionresults(self):
        """
        返回学生的选课结果
        :return:list
                ((2001, '数据库', 4, 13, '一教101'),)
        """
        return electresult(self.id)

    def selectplain(self):
        """
        返回学生能选课程
        :return: 每个课程包括课程号，课程名，学分，上课时间，地点，可选人数，已选人数
                ((2001, '数据库', 4, 13, '一教101', 30, 0),)
        """
        res = Trainplain(self.major, self.grade)
        lis = []
        for i in range(len(res)):
            k = list(res[0])
            l = k[3] // 10
            r = k[3] % 10
            k[3] = "%s~%s" % (self.time[l], self.time[r])
            lis.append(k)
        return lis

    def searchcourse(self, coursename):
        """
        :param coursename: 搜索的课程名，不需要全名
        :return: 返回搜索到的课程
                ((2001, '数据库', 4, 13, '一教101', 30, 0),)
        """
        res = SearchCourse(coursename)
        lis = []
        for i in range(len(res)):
            k = list(res[0])
            l = k[3] // 10
            r = k[3] % 10
            k[3] = "%s~%s" % (self.time[l], self.time[r])
            lis.append(k)
        return lis

# app = Student(50001, '软件与物联网工程学院', '软件工程', '软件工程', 2)
# print(app.searchcourse('据'))
