# import logic.login as llogin
from PyQt5.QtWidgets import QMainWindow

import originalUIFile.adminHome as uadminHome
import ui.realizeLogin as uLogin


class AdminHomeWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uadminHome.Ui_Dialog(self)
        self.setWindowTitle('管理员主界面')

    def test(self):
        pass

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()
