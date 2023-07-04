from PyQt5.QtWidgets import QMainWindow

import originalUIFile.teacherHome as uTeacherHome
import ui.realizeLogin as uLogin


class TeacherHomeWindow(QMainWindow):
    def __init__(self, teacher, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uTeacherHome.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.setWindowTitle('教师主界面')
        self.teacher = teacher  # 学生对象
        # 用户一进入主界面就显示任课结果
        # self.ui.showSearchResult

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.logOutButton.clicked.connect(self.logOut)
        self.ui.feedbackButton.clicked.connect(self.feedback)
        self.ui.selfInformButton.clicked.connect(self.getSelfInform)

    def getSelfInform(self):
        """
        获取教师信息
        :return: None
        """
        pass

    def feedback(self):
        """
        反馈按钮槽函数
        :return: None
        """
        pass

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()
