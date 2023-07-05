# QCursor
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
# Qmenu
from PyQt5.QtWidgets import QMenu

import originalUIFile.selectedSubsWindow as uSelectedSubsWindow


# QAction


class SelectedSubsWindow(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uSelectedSubsWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('已选课程')
        self.student = student  # 学生对象
        self.slot_init()
        # 用户一进入主界面就显示可选课程
        self.rightMenuInit()
        self.showSearchResult()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        pass

    def showSearchResult(self):
        """
        显示搜索结果
        :return: None
        """
        # 选课编号  课程号，课程名，学分，时间（时），地点，老师姓名，时间（天）
        # [[1, 2002, '数据结构', 4, '8:00~10:00', '一教101', '老王', '周三']]
        data = self.student.selectionresults()
        if not data:
            QtWidgets.QMessageBox.information(self, '提示', '选课清单为空', QtWidgets.QMessageBox.Ok)
            self.deleteLater()
            return
        # 测试数据
        # data = [[1, 2002, '数据结构', 4, '8:00~10:00', '一教101', '老王', '周三'], [2, 2003, '操作系统', 4, '10:00~12:00', '一教102', '老李', '周四']]
        # 显示在表格中
        self.ui.showSelectedSubs.setRowCount(len(data))
        self.ui.showSelectedSubs.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.ui.showSelectedSubs.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
        # 设置表头
        self.ui.showSelectedSubs.setHorizontalHeaderLabels(
            ['选课编号', '课程号', '课程名', '学分', '时间', '地点', '老师姓名', '星期'])
        # 设置表格不可编辑
        self.ui.showSelectedSubs.setEditTriggers(self.ui.showSelectedSubs.NoEditTriggers)
        # 设置右键菜单，可以退选课程
        self.ui.showSelectedSubs.setContextMenuPolicy(3)
        self.ui.showSelectedSubs.customContextMenuRequested.connect(self.rightMenuShow)
        # 设置表格自适应大小
        self.ui.showSelectedSubs.horizontalHeader().setSectionResizeMode(1)
        # 不显示行号
        # self.ui.showSelectedSubs.verticalHeader().setVisible(False)

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
        # 创建右键菜单
        self.contextMenu = QMenu()
        # 创建菜单选项
        self.actionA = self.contextMenu.addAction('退选课程')
        # 将菜单选项与槽函数连接
        self.actionA.triggered.connect(self.actionHandler)

    def actionHandler(self):
        """
        菜单选项槽函数
        :return: None
        """
        # 获取当前选中的行
        row = self.ui.showSelectedSubs.currentRow()
        # 获取当前选中的课程号
        sub_id = self.ui.showSelectedSubs.item(row, 0).text()
        # 退选课程
        self.student.withdrawalcourse(int(sub_id))
        # 刷新显示
        self.showSearchResult()

