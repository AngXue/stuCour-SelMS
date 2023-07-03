import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import ui.stuHome as uStuhome


class StuHome(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uStuhome.Ui_Dialog(self)
        self.setWindowTitle('学生主界面')
        self.student = student  # 学生对象
        # self.ui.showSearchResult

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        pass

    def getSelfInform(self):
        """
        获取个人信息按钮槽函数
        :return: None
        """
        pass

    def getSelectedSubs(self):
        """
        获取已选课程按钮槽函数
        :return: None
        """
        pass

    def searchSubs(self):
        """
        搜索课程按钮槽函数
        :return: None
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StuHome()
    win.show()
    sys.exit(app.exec_())
