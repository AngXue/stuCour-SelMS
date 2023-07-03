# 主程序

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import ui.login as ulogin
import ui.realizeStuHome
import logic.login as llogin


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
        stu = llogin.login(userName, userPasswd)
        uStuHome = ui.realizeStuHome.StuHome(stu)
        uStuHome.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec_())
