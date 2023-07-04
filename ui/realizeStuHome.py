from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import originalUIFile.stuHome as uStuhome
import ui.realizeLogin as uLogin
import ui.realizeSelectedSubsWindow as uSelectedSubsWindow
import ui.realizeUserInformWindow as uUserInformWindow
import logic.student as lstudent


class StuHome(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uStuhome.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('学生主界面')
        self.student = student  # 学生对象
        self.slot_init()
        # 用户一进入主界面就显示可选课程
        self.showCanSelectSubs()

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

    def showCanSelectSubs(self):
        """
        显示可选课程
        :return:
        """
        # data数据形式 ((2001, '数据库', 4, 13, '一教101', 30, 0),)
        # 测试数据
        data = ((2001, '数据库', 4, 13, '一教101', 30, 0), (2002, '数据库', 4, 13, '一教101', 30, 0))
        # data = self.student.getCanSelectSubs()  # TODO: 调用学生对象的获取可选课程函数
        # 将数据显示在表格中
        self.ui.showSearchResult.setRowCount(len(data))
        self.ui.showSearchResult.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.ui.showSearchResult.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        # 设置表头
        self.ui.showSearchResult.setHorizontalHeaderLabels(
            ['课程ID', '课程名', '学分', '上课时间', '上课地点', '可选人数', '已选人数'])
        # 设置表格不可编辑
        self.ui.showSearchResult.setEditTriggers(self.ui.showSearchResult.NoEditTriggers)

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
