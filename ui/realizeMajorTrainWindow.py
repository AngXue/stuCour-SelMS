from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
import originalUIFile.majorTrainWindow as uMajorTrain


class MajorTrainWindow(QMainWindow):
    def __init__(self, header, showData, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uMajorTrain.Ui_Dialog()
        self.ui.setupUi(self)
        self.header = header  # 表头
        self.showData = showData  # 专业培养方案信息
        self.slot_init()
        self.setWindowTitle('专业培养方案')
        self.showMajorTrain()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        pass

    def showMajorTrain(self):
        """
        显示专业培养方案
        :return: None
        """
        # self.showData 课程号 课程名 学分 专业名 学期
        # 测试数据 [['1', '高等数学', '5', '计算机科学与技术', '1'], ['2', '线性代数', '4', '计算机科学与技术', '1']]
        # 将self.showData显示在self.ui.showMajorTrainResult中
        # 设置表头
        self.ui.showMajorTrainResult.setRowCount(len(self.showData))
        self.ui.showMajorTrainResult.setColumnCount(len(self.showData[0]))
        self.ui.showMajorTrainResult.setHorizontalHeaderLabels(self.header)
        # 设置表格内容
        for i in range(len(self.showData)):
            for j in range(len(self.header)):
                self.ui.showMajorTrainResult.setItem(i, j, QtWidgets.QTableWidgetItem(self.showData[i][j]))
        # 设置表格自适应宽度
        self.ui.showMajorTrainResult.horizontalHeader().setSectionResizeMode(1)
        # 设置表格不可编辑
        self.ui.showMajorTrainResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
