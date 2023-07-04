from PyQt5.QtWidgets import QMainWindow

import originalUIFile.teacherHome as uTeacherHome
import ui.realizeLogin as uLogin


class TeacherHomeWindow(QMainWindow):
    def __init__(self, teacher, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uTeacherHome.Ui_Dialog(self)
        self.setWindowTitle('教师主界面')
        self.teacher = teacher  # 学生对象
        # self.ui.showSearchResult

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
