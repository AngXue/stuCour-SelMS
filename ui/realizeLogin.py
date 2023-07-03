# import logic.login as llogin
from PyQt5.QtWidgets import QMainWindow

import originalUIFile.login as ulogin
import ui.realizeAdminHome
import ui.realizeStuHome


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = ulogin.Ui_MainWindow(self)
        self.setWindowTitle('学生选课管理系统')

    def login(self):
        """
        登录按钮槽函数
        :return: None
        """

        # 从输入框获取用户名和密码
        userName = self.ui.loginNameInput.text()
        userPasswd = self.ui.loginPasswdInput.text()
        # 测试用
        # user = llogin.login(userName, userPasswd)
        user = None
        self.stuHome = ui.realizeStuHome.StuHome(user)
        # self.adminHome = ui.realizeAdminHome.AdminHomeWindow()
        self.hide()
        self.stuHome.show()
        # self.adminHome.show()
