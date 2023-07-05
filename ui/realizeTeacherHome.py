from PyQt5.QtWidgets import QMainWindow
# 导入QmessageBox
from PyQt5.QtWidgets import QTableWidgetItem

import originalUIFile.teacherHome as uTeacherHome
import ui.realizeLogin as uLogin
import ui.realizeTeacherFeedBack as uTeacherFeedback
import ui.realizeUserInformWindow as uUserInformWindow


class TeacherHomeWindow(QMainWindow):
    def __init__(self, teacher, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uTeacherHome.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.setWindowTitle('教师主界面')
        self.teacher = teacher  # 学生对象
        self.uUserInformWindow = uUserInformWindow.UserInformWindow(self.teacher)
        self.uTeacherFeedback = uTeacherFeedback.TeacherFeedbackWindow(self.teacher)
        # 用户一进入主界面就显示任课结果
        self.showTeachResult()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.logOutButton.clicked.connect(self.logOut)
        self.ui.feedbackButton.clicked.connect(self.feedback)
        self.ui.selfInformButton.clicked.connect(self.showSelfInform)

    def showTeachResult(self):
        """
        显示任课结果
        ((1, 2001, '数据库', 4, 10:00~12:00, '一教101', 0),)
        :return: None
        """
        data = self.teacher.searchteaching()
        if not data:
            return
        # 测试数据
        # data = ((1, 2001, '数据库', 4, '10:00~12:00', '一教101', 0), (2, 2002, '数据结构', 4, '10:00~12:00', '一教101', 0))
        self.ui.showTeacherSubsResult.setRowCount(len(data))
        self.ui.showTeacherSubsResult.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.ui.showTeacherSubsResult.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        # 设置表头
        self.ui.showTeacherSubsResult.setHorizontalHeaderLabels(
            ['课程编号', '课程ID', '课程名称', '学分', '学时', '上课地点', '已选人数'])
        # 设置表格为禁止编辑
        self.ui.showTeacherSubsResult.setEditTriggers(self.ui.showTeacherSubsResult.NoEditTriggers)
        # 设置表格自适应
        self.ui.showTeacherSubsResult.horizontalHeader().setSectionResizeMode(1)

    def showSelfInform(self):
        """
        获取教师信息
        :return: None
        """
        self.uUserInformWindow.show()

    def feedback(self):
        """
        反馈按钮槽函数
        :return: None
        """
        self.uTeacherFeedback.show()

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        # 如果self.uUserInformWindow存在, 则关闭
        if self.uUserInformWindow:
            self.uUserInformWindow.close()
        # 如果self.uTeacherFeedback存在, 则关闭
        if self.uTeacherFeedback:
            self.uTeacherFeedback.close()
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()
