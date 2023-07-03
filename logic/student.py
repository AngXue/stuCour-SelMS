from dataBaseControl.data import *


class Student:
    def __init__(self, id, name, college, major, grade):
        self.id = id
        self.name = name
        self.college = college
        self.major = major
        self.grade = grade

    def selectionresults(self):
        '''
        返回学生的选课结果
        :return:list
        '''
        return electresult(self.id)
