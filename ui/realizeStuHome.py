from PyQt5.QtWidgets import QMainWindow

import originalUIFile.stuHome as uStuhome
import ui.realizeLogin as uLogin


class StuHome(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uStuhome.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('学生主界面')
        self.student = student  # 学生对象
        self.slot_init()
        # 用户一进入主界面就显示可选课程
        # self.ui.showSearchResult

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.logOutButton.clicked.connect(self.logOut)
        self.ui.selfInformButton.clicked.connect(self.getSelfInform)
        self.ui.selectedButton.clicked.connect(self.getSelectedSubs)
        self.ui.searchSubsButton.clicked.connect(self.searchSubs)

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()

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
