from PyQt5.QtWidgets import QMainWindow

import originalUIFile.stuHome as uStuhome
import ui.realizeLogin as uLogin
import ui.realizeUserInformWindow as uUserInformWindow
import ui.realizeSelectedSubsWindow as uSelectedSubsWindow


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
        self.ui.selfInformButton.clicked.connect(self.showSelfInform)
        self.ui.selectedButton.clicked.connect(self.showSelectedSubs)
        self.ui.searchSubsButton.clicked.connect(self.searchSubs)
        self.ui.searchSubsInput.returnPressed.connect(self.searchSubs)
        self.ui.searchSubsInput.setPlaceholderText('请输入课程名称(完整ID或部分名称)')
        txt = "此处显示搜索结果"
        self.ui.showSearchResult.setText(
            '<html><head/><body><p align="center">{}<span style=" font-size:12pt;">'.format(txt))

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()

    def showSelfInform(self):
        """
        个人信息按钮槽函数
        :return: None
        """
        self.userInformWindow = uUserInformWindow.UserInformWindow(self.student)
        self.userInformWindow.show()

    def showSelectedSubs(self):
        """
        获取已选课程按钮槽函数
        :return: None
        """
        self.selectedSubsWindow = uSelectedSubsWindow.SelectedSubsWindow(self.student)
        self.selectedSubsWindow.show()

    def searchSubs(self):
        """
        搜索课程按钮槽函数
        :return: None
        """
        pass
