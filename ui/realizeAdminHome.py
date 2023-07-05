from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QCursor

import originalUIFile.adminHome as uadminHome
import ui.realizeAdminColMana as uAdminColMana
import ui.realizeAdminCourMana as uAdminCourMana
import ui.realizeLogin as uLogin


class AdminHomeWindow(QMainWindow):
    def __init__(self, admin, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uadminHome.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.admin = admin  # 管理员对象
        self.rightMenuInit()
        self.setWindowTitle('管理员主界面')
        self.adminColManaWindow = uAdminColMana.AdminColManaWindow(self.admin)
        self.adminCourManaWindow = uAdminCourMana.AdminCourseManageWindow(self.admin)

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.manageCollegeInformButton.clicked.connect(self.manageCollegeInform)
        self.ui.deleteUsersButton.clicked.connect(self.deleteUsers)
        self.ui.manageSubsInformButton.clicked.connect(self.manageSubsInform)
        self.ui.startSelectSubsButton.clicked.connect(self.startSelectSubs)
        self.ui.searchUsersButton.clicked.connect(self.searchUsers)
        self.ui.stopSelectSubsButton.clicked.connect(self.stopSelectSubs)
        self.ui.uploadStusInformButton.clicked.connect(self.uploadStusInform)
        self.ui.uploadTeachersInformButton.clicked.connect(self.uploadTeachersInform)
        self.ui.logOutButton.clicked.connect(self.logOut)
        self.ui.searchUsersInput.returnPressed.connect(self.searchUsers)
        # 设置提示信息
        self.ui.searchUsersInput.setPlaceholderText('请输入需要搜索的用户的ID或姓名')

    def manageCollegeInform(self):
        """
        学院信息管理按钮槽函数
        :return: None
        """
        self.adminColManaWindow.show()

    def deleteUsers(self):
        """
        删除用户按钮槽函数
        :return: None
        """
        # 获取需删除的用户ID起始值和结束值
        startID = self.ui.deleteStartInput.text()
        endID = self.ui.deleteEndInput.text()
        # 删除用户
        self.admin.deletefomatin(startID, endID)

    def manageSubsInform(self):
        """
        课程信息管理按钮槽函数
        :return: None
        """
        self.adminCourManaWindow.show()

    def startSelectSubs(self):
        """
        开启选课按钮槽函数
        :return: None
        """
        self.admin.opencourse()

    def searchUsers(self):
        """
        查询用户按钮槽函数
        :return: None
        """
        # 当用户点击self.ui.searchUsersInput时，清空输入框
        if self.ui.searchUsersInput.text() == '请输入需要搜索的用户的ID或姓名':
            self.ui.searchUsersInput.clear()
        # 获取用户输入的信息
        searchInfo = self.ui.searchUsersInput.text()
        # 查询用户
        if searchInfo == '':
            return
        data = self.admin.queryinfomation(searchInfo)
        # 数据 [[1001, '老杰', '艺术学院', '硕士研究生', '博士学位', 'teacher'], [50001, '陈名杰', '软件与物联网工程', '软件工程', 'student']]
        # 测试数据
        # data = [[1001, '老杰', '艺术学院', '硕士研究生', '博士学位', 'teacher'], [50001, '陈名杰', '软件与物联网工程', '本科生', '软件工程', 'student']]
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
        # 设置表头
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', '姓名', '学院', '专业', '学位', '身份'])
        # 设置表格不可编辑
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 设置表格自适应
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1)
        # 右键菜单，可以删除用户
        self.ui.tableWidget.setContextMenuPolicy(3)
        self.ui.tableWidget.customContextMenuRequested.connect(self.rightMenuShow)

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
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction('删除用户')
        self.actionA.triggered.connect(self.selectSubs)

    def selectSubs(self):
        """
        删除用户
        :return: None
        """
        # 获取选中的行
        row = self.ui.tableWidget.currentRow()
        # 获取选中行的第一列的内容
        _id = self.ui.tableWidget.item(row, 0).text()
        # 删除用户
        self.admin.deletefomatin(_id, _id)

    def stopSelectSubs(self):
        """
        停止选课按钮槽函数
        :return: None
        """
        self.admin.closecourse()

    def uploadStusInform(self):
        """
        上传学生信息按钮槽函数
        :return: None
        """
        # 打开文件选择对话框
        # 获取文件路径
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        self.admin.uploadstudent(filePath)

    def uploadTeachersInform(self):
        """
        上传教师信息按钮槽函数
        :return: None
        """
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        self.admin.uploadteacher(filePath)

    def logOut(self):
        """
        登出按钮槽函数
        :return: None
        """
        # 如果self.adminColManaWindow存在，则关闭
        if self.adminColManaWindow:
            self.adminColManaWindow.close()
        # 如果self.adminCourManaWindow存在，则关闭
        if self.adminCourManaWindow:
            self.adminCourManaWindow.close()
        self.deleteLater()
        self.loginWindow = uLogin.LoginWindow()
        self.loginWindow.show()
