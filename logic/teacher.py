from dataBaseControl.DataTeacher import *

class teacher:

    time=["","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]

    def __init__(self,id,name,education,degree,collegeID,college):
        self.ID=id
        self.name=name
        self.education=education
        self.degree=degree
        self.collegeID=collegeID
        self.college=college

    #返回老师信息信息
    def selfinfomation(self):
        '''
        返回个人信息
        :return: 工号，姓名，学历，学位，学院号，学院名
        '''
        return [self.ID,self.name,self.education,self.degree,self.collegeID,self.college]

    #发送反馈老师信息
    def feedback(self,messege):
        feedbackmessege(self.name,messege)
    #查找任课表
    def searchteaching(self):
        '''

        :return: 返回任课结果
                ((2001, '数据库', 4, 13, '一教101', 0),)
        '''
        res=SearchTeaching(self.name)
        lis=[]
        for i in range (len(res)):
            k=list(res[0])
            l=k[3]//10
            r=k[3]%10
            k[3]="%s~%s"%(self.time[l],self.time[r])
            lis.append(k)
        return lis


# app=teacher(10001,'老王','硕士研究生','博士学位',101,'软件与物联网工程学院')
# print(app.searchteaching())
