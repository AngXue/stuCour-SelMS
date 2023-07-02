# 主程序

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.login import *


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # self.ui.loginbutton.clicked.connect()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
