from PyQt5.QtWidgets import QMainWindow

import originalUIFile.adminHome as uadminHome
import ui.realizeLogin as uLogin


class AdminHomeWindow(QMainWindow):
    def __init__(self, admin, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uadminHome.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.admin = admin  # 管理员对象
        self.setWindowTitle('管理员主界面')

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.manageCollegeInformButton.clicked.connect(self.manageCollegeInform)
        self.ui.deleteUsersButton.clicked.connect(self.deleteUsers)
        self.ui.manageSubsInformButton.clicked.connect(self.manageSubsInform)
        self.ui.startSelectSubsButton.clicked.connect(self.startSelectSubs)
        self.ui.searchUsersButton.clicked.connect(self.searchUsers)
        self.ui.stopSelectSubsButton.clicked.connect(self.stopSelectSubs)
        self.ui.uploadStusInformButton.clicked.connect(self.uploadStusInform)
        self.ui.uploadTeachersInformButton.clicked.connect(self.uploadTeachersInform)
        self.ui.logOutButton.clicked.connect(self.logOut)

    def manageCollegeInform(self):
        """
        学院信息管理按钮槽函数
        :return: None
        """
        pass

    def deleteUsers(self):
        """
        删除用户按钮槽函数
        :return: None
        """
        pass

    def manageSubsInform(self):
        """
        课程信息管理按钮槽函数
        :return: None
        """
        pass

    def startSelectSubs(self):
        """
        开启选课按钮槽函数
        :return: None
        """
        pass

    def searchUsers(self):
        """
        查询用户按钮槽函数
        :return: None
        """
        pass

    def stopSelectSubs(self):
        """
        停止选课按钮槽函数
        :return: None
        """
        pass

    def uploadStusInform(self):
        """
        上传学生信息按钮槽函数
        :return: None
        """
        pass

    def uploadTeachersInform(self):
        """
        上传教师信息按钮槽函数
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
