from dataBaseControl.data import *


class Student:
    def __init__(self, id, name, college, major, grade):
        self.id = id
        self.name = name
        self.college = college
        self.major = major
        self.grade = grade

    def selfinfomation(self):
        '''
        返回学生基本信息
        :return: 学号，姓名，学院，专业，年级
        '''

        return [self.id, self.name, self.college, self.major, self.grade]

    def selectionresults(self):
        '''
        返回学生的选课结果
        :return:list
        '''
        print(electresult(self.id))

    def selectplain(self):
        '''
        返回学生能选课程
        :return: 每个课程包括课程号，课程名，学分，上课时间，地点，可选人数，已选人数
                ((2001, '数据库', 4, 13, '一教101', 30, 0),)
        '''
        return Trainplain(self.major, self.grade)


# app = Student(50001, '软件与物联网工程学院', '软件工程', '软件工程', 2)
# app.selectionresults()
