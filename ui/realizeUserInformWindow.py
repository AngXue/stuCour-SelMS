from PyQt5.QtWidgets import QMainWindow

import originalUIFile.userInformWindow as uUserInformWindow


class UserInformWindow(QMainWindow):
    def __init__(self, user, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uUserInformWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('个人信息')
        self.user = user  # 用户对象
        self.slot_init()
        self.showInform()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        pass

    def showInform(self):
        """
        显示个人信息
        :return: None
        """
        self.ui.showSelfInform.setText(
            '<html><head/><body><p align="center">ID: {}<span style=" font-size:12pt;">'.format(self.user[1]))
