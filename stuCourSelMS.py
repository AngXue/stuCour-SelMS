# 主程序

import sys

from PyQt5.QtWidgets import QApplication

import ui.realizeLogin as uLogin
import ui.realizeTeacherHome as uTeacherHome
import ui.realizeAdminHome as uAdminHome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = uLogin.LoginWindow()
    # win = uAdminHome.AdminHomeWindow(None)
    win.show()
    sys.exit(app.exec_())
