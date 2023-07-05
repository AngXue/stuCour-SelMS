from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTreeWidgetItem

import originalUIFile.adminCollegeManage as uAdminColMana
import ui.realizeMajorTrainWindow as uMajorTrain


class AdminColManaWindow(QMainWindow):
    def __init__(self, admin, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uAdminColMana.Ui_Dialog()
        self.ui.setupUi(self)
        self.admin = admin  # 管理员对象
        self.uMajorTrainWindow = None  # 专业培养方案窗口
        self.slot_init()
        self.setWindowTitle('学院信息管理')
        self.showCollegeInform()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.uploadCollegeMajorButton.clicked.connect(self.uploadCollegeAndMajorInform)
        self.ui.uploadTrainButton.clicked.connect(self.uploadTrainInform)

    def uploadTrainInform(self):
        """
        上传培养方案按钮槽函数
        :return: None
        """
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        self.admin.uploadTrainInform(filePath)

    def uploadCollegeAndMajorInform(self):
        """
        上传学院和专业信息按钮槽函数
        :return: None
        """
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        self.admin.uploadCollegeAndMajorInform(filePath)

    def showCollegeInform(self):
        """
        显示学院信息
        将学院、专业显示在self.ui.showCollegeResult中
        self.ui.showCollegeResult是一个QTreeWidget对象
        :return: None
        """
        # 学院信息：学院ID、学院名称
        collegeList = self.admin.searchcollege()
        # 测试数据
        # collegeList = [['1', '计算机学院'], ['2', '软件学院']]
        # 显示学院信息
        # 添加学院节点，然后分别将其专业添加为子节点
        for college in collegeList:
            collegeNode = QTreeWidgetItem(self.ui.showCollegeResult)
            # 每个学院节点的文本：计算机学院 [1]
            collegeNodeStr = str(college[1]) + ' [' + str(college[0]) + ']'
            collegeNode.setText(0, collegeNodeStr)  # 设置第一列的文本
            # 添加专业节点
            # 专业节点的文本：计算机科学与技术
            # 将计算机科学与技术和软件工程添加为计算机学院的子节点
            # 专业信息：专业名称
            majorList = self.admin.searchmajor(college[0])
            # 测试数据
            # majorList = ['计算机科学与技术', '软件工程']
            for major in majorList:
                majorNode = QTreeWidgetItem(collegeNode)
                majorNode.setText(0, major)
        # 设置最顶层节点的文本
        self.ui.showCollegeResult.setHeaderLabel('学院信息')
        # 设置初始状态全部展开
        self.ui.showCollegeResult.expandAll()
        # 右键菜单， 鼠标右键点击学院节点，弹出菜单，可以删除学院
        # 鼠标右键点击专业节点，弹出菜单，可以删除专业、查看培养方案
        self.ui.showCollegeResult.setContextMenuPolicy(3)
        self.ui.showCollegeResult.customContextMenuRequested.connect(self.showCollegeResultMenu)

    def showCollegeResultMenu(self):
        """
        学院信息右键菜单
        :return: None
        """
        menu = QtWidgets.QMenu()
        # 判断选中的是学院还是专业
        # 选中的是学院
        if self.ui.showCollegeResult.currentItem().parent() is None:
            # 删除学院
            delCollegeAction = menu.addAction('删除学院')
            delCollegeAction.triggered.connect(self.delCollege)
        # 选中的是专业
        else:
            # 删除专业
            delMajorAction = menu.addAction('删除专业')
            delMajorAction.triggered.connect(self.delMajor)
            # 查看培养方案
            showTrainProgramAction = menu.addAction('查看培养方案')
            showTrainProgramAction.triggered.connect(self.showTrainProgram)
        menu.exec_(QtGui.QCursor.pos())

    def showTrainProgram(self):
        """
        查看培养方案
        :return:
        """
        # 获取专业所属学院ID和专业名称
        collegeID = self.ui.showCollegeResult.currentItem().parent().text(0).split('[')[1].split(']')[0]
        majorName = self.ui.showCollegeResult.currentItem().text(0)
        data = self.admin.showTrainProgram(collegeID, majorName)
        # 课程号 课程名 学分 专业名 学期
        # 测试数据
        header = ['课程号', '课程名', '学分', '专业名', '学期']
        # data = [['1', '高等数学', '5', '计算机科学与技术', '1'], ['2', '线性代数', '4', '计算机科学与技术', '1']]
        self.uMajorTrainWindow = uMajorTrain.MajorTrainWindow(header, data)
        self.uMajorTrainWindow.show()

    def delMajor(self):
        """
        删除专业
        :return:
        """
        # 获取专业所属学院ID和专业名称
        collegeID = self.ui.showCollegeResult.currentItem().parent().text(0).split('[')[1].split(']')[0]
        majorName = self.ui.showCollegeResult.currentItem().text(0)
        self.admin.delMajor(collegeID, majorName)

    def delCollege(self):
        """
        删除学院
        :return:
        """
        # 获取学院ID
        collegeID = self.ui.showCollegeResult.currentItem().text(0).split('[')[1].split(']')[0]
        self.admin.delCollege(collegeID)

    def closeEvent(self, event):
        """
        重写closeEvent函数
        :param event:
        :return:
        """
        if self.uMajorTrainWindow is not None:
            self.uMajorTrainWindow.close()
        event.accept()
