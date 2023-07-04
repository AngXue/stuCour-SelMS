from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QCursor

import originalUIFile.adminCourseManage as uadminCourseManage


class AdminCourseManageWindow(QMainWindow):
    def __init__(self, admin, parent=None):
        super(AdminCourseManageWindow, self).__init__(parent)
        self.ui = uadminCourseManage.Ui_Dialog()
        self.ui.setupUi(self)
        self.admin = admin  # 管理员对象
        self.setWindowTitle('课程管理')
        self.rightMenuInit()
        self.slot_init()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.uploadCourseButton.clicked.connect(self.uploadCourse)
        self.ui.courseSearchButton.clicked.connect(self.courseSearch)
        self.ui.setCourseteacherButton.clicked.connect(self.setCourseteacher)
        self.ui.setSubTeacherInput.returnPressed.connect(self.setCourseteacher)
        # 设置提示信息
        self.ui.setSubTeacherInput.setPlaceholderText('新的课程教师ID')
        self.ui.adminSearchCourse.setPlaceholderText('请输入需要搜索的课程ID或名称')

    def showResult(self, showData, showDataHeader, resizeMode=1):
        """
        显示查询结果
        :param showDataHeader:  表头
        :param showData: 查询结果
        :param resizeMode: 1: 表格内容自适应 2: 表格宽度自适应 3: 表格内容和宽度都自适应
        :return:
        """
        # 将数据显示在表格中
        self.ui.showSearchSubsResult.setRowCount(len(showData))
        self.ui.showSearchSubsResult.setColumnCount(len(showData[0]))
        for i in range(len(showData)):
            for j in range(len(showData[i])):
                self.ui.showSearchSubsResult.setItem(i, j, QTableWidgetItem(str(showData[i][j])))
        # 设置表头
        self.ui.showSearchSubsResult.setHorizontalHeaderLabels(showDataHeader)
        # 设置表格不可编辑
        self.ui.showSearchSubsResult.setEditTriggers(self.ui.showSearchSubsResult.NoEditTriggers)
        # 右键菜单
        self.ui.showSearchSubsResult.setContextMenuPolicy(3)
        self.ui.showSearchSubsResult.customContextMenuRequested.connect(self.rightMenuShow)
        # 设置表格内容自适应
        # self.ui.showSearchSubsResult.resizeColumnsToContents()
        # self.ui.showSearchSubsResult.resizeRowsToContents()
        # 设置表格自适应宽度
        self.ui.showSearchSubsResult.horizontalHeader().setSectionResizeMode(1)

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
        self.actionA = self.contextMenu.addAction('删除课程')
        self.actionA.triggered.connect(self.deleteCourse)

    def setCourseteacher(self):
        """
        设置课程教师
        :return:
        """
        pass

    def uploadCourse(self):
        """
        上传课程
        :return:
        """
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        # self.admin.uploadcourse(filePath) # TODO: 连接数据库

    def deleteCourse(self):
        """
        删除课程
        选课编号 ，课程号，课程名，学分，上课时间（时），地点，可选人数，已选人数，年级，开课专业，老师姓名，上课时间（天）
        :return:
        """
        # 获取当前选中的行
        currentRow = self.ui.showSearchSubsResult.currentRow()
        # 获取当前选中的选课编号
        subId = self.ui.showSearchSubsResult.item(currentRow, 0).text()
        # self.admin.deleteCourse(subId) # TODO: 连接数据库

    def courseSearch(self):
        """
        课程查询
        选课编号 ，课程号，课程名，学分，时间，地点，可选人数，已选人数，年级，开课专业，教师姓名，星期
        :return:
        """
        # data = self.admin.searchCourse() # TODO: 连接数据库
        # 测试数据
        data = [[1, 2002, '数据结构', '~11:00', 13, '一教101', 30, 0, 2, '软件工程', '老王', '周三']]
        dataHeader = ['选课编号', '课程号', '课程名', '时间', '学分', '地点', '可选人数', '已选人数', '年级', '开课专业', '教师姓名', '星期']
        self.showResult(data, dataHeader)

