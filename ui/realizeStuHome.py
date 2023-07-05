from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QTableWidgetItem
# 导入 QmessageBox
from PyQt5.QtWidgets import QMessageBox

import originalUIFile.stuHome as uStuhome
import ui.realizeLogin as uLogin
import ui.realizeSelectedSubsWindow as uSelectedSubsWindow
import ui.realizeUserInformWindow as uUserInformWindow


class StuHome(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uStuhome.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('学生主界面')
        self.student = student  # 学生对象
        self.slot_init()
        # 用户一进入主界面就显示可选课程
        self.rightMenuInit()
        self.showCanSelectSubs()
        self.userInformWindow = uUserInformWindow.UserInformWindow(self.student)
        self.selectedSubsWindow = None

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

    def showResult(self, showData, showDataHeader, resizeMode=1):
        """
        显示查询结果
        :param showDataHeader:  表头
        :param showData: 查询结果
        :param resizeMode: 1: 表格内容自适应 2: 表格宽度自适应 3: 表格内容和宽度都自适应
        :return:
        """
        if not showData:
            QMessageBox.information(self, '提示', '未查询到结果', QMessageBox.Ok)
            return
        # 将数据显示在表格中
        self.ui.showSearchResult.setRowCount(len(showData))
        self.ui.showSearchResult.setColumnCount(len(showData[0]))
        for i in range(len(showData)):
            for j in range(len(showData[i])):
                self.ui.showSearchResult.setItem(i, j, QTableWidgetItem(str(showData[i][j])))
        # 设置表头
        self.ui.showSearchResult.setHorizontalHeaderLabels(showDataHeader)
        # 设置表格不可编辑
        self.ui.showSearchResult.setEditTriggers(self.ui.showSearchResult.NoEditTriggers)
        # 右键菜单可以选课
        self.ui.showSearchResult.setContextMenuPolicy(3)
        self.ui.showSearchResult.customContextMenuRequested.connect(self.rightMenuShow)
        # 设置表格内容自适应
        # self.ui.showSearchResult.resizeColumnsToContents()
        # self.ui.showSearchResult.resizeRowsToContents()
        # 设置表格自适应宽度
        self.ui.showSearchResult.horizontalHeader().setSectionResizeMode(resizeMode)

    def showCanSelectSubs(self):
        """
        显示可选课程
        :return:
        """
        data = self.student.selectplain()
        # 课程编号，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
        # 测试数据
        header = ['选课编号', '课程号', '课程名', '学分', '时间', '地点', '可选人数', '已选人数', '年级', '开课专业', '老师姓名', '星期']
        # data = [[1, '数据结构', 3, '~11:00', '一教101', 30, 0, 2, '软件工程', '可林', '周三']]
        self.showResult(data, header, 3)

    def rightMenuShow(self):
        """
        右键菜单显示
        :return: None
        """
        # 获取鼠标点击的位置
        pos = QCursor.pos()
        # 在鼠标位置显示
        self.contextMenu.exec_(pos)

    def rightMenuInit(self):
        """
        右键菜单初始化
        :return: None
        """
        self.contextMenu = QMenu()
        self.actionA = self.contextMenu.addAction('选课')
        self.actionA.triggered.connect(self.selectSubs)

    def selectSubs(self):
        """
        选课槽函数
        选课编号 ，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
        :return: None
        """
        # 获取选中的课程选课编号
        selectSubsID = self.ui.showSearchResult.item(self.ui.showSearchResult.currentRow(), 0).text()
        # 获取选中的课程名
        selectSubsName = self.ui.showSearchResult.item(self.ui.showSearchResult.currentRow(), 2).text()
        # 获取Weektime, Daytime
        Weektime = self.ui.showSearchResult.item(self.ui.showSearchResult.currentRow(), 11).text()
        time = ["", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
        # 假如课程时间是13:00~15:00，那么Daytime=68，取13:00在time中的索引值，即6，取15:00在time中的索引值，即8，Daytime=68
        Daytime = self.ui.showSearchResult.item(self.ui.showSearchResult.currentRow(), 4).text()
        numOne = time.index(Daytime.split('~')[0])
        numTwo = time.index(Daytime.split('~')[1])
        Daytime = numOne * 10 + numTwo
        # 调用学生对象的选课函数
        if self.student.choosecourse(int(selectSubsID), selectSubsName, Weektime, int(Daytime)):
            QMessageBox.information(self, '提示', '选课成功！')
        else:
            QMessageBox.information(self, '提示', '选课失败！')

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        # 如果self.userInformWindow存在，关闭
        if self.userInformWindow:
            self.userInformWindow.close()
        # 如果self.selectedSubsWindow存在，关闭
        # if self.selectedSubsWindow is not None:
        #     self.selectedSubsWindow.close()
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()

    def showSelfInform(self):
        """
        个人信息按钮槽函数
        :return: None
        """
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
        # 获取搜索框中的内容
        searchContent = self.ui.searchSubsInput.text()
        # 如果搜索框中没有内容， 显示所有可选课程
        if searchContent == '':
            self.showCanSelectSubs()
            return
        searchData = self.student.searchcourse(searchContent)
        # 选课编号 ，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
        # [[1, 2002, '数据结构', '~11:00', 13, '一教101', 30, 0, 2, '软件工程', '老王', '周三']]
        # 测试数据
        header = ['课程ID', '课程名', '学分', '上课时间', '学时', '上课地点', '容量', '已选人数', '年级', '开课专业',
                  '教师名', '上课时间']
        # searchData = [[1, 2002, '数据结构', '~11:00', 13, '一教101', 30, 0, 2, '软件工程', '搜王', '周三']]
        self.showResult(searchData, header, 3)
