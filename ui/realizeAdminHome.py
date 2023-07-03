# import logic.login as llogin
from PyQt5.QtWidgets import QMainWindow

import ui.adminHome as uadminHome


class AdminHome(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uadminHome.Ui_Dialog(self)
        self.setWindowTitle('管理员主界面')

    def test(self):
        pass
