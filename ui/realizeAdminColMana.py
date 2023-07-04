from PyQt5.QtWidgets import QMainWindow

import originalUIFile.adminCollegeManage as uAdminColMana


class AdminColManaWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uAdminColMana.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.setWindowTitle('学院信息管理')

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.addCollegeButton.clicked.connect(self.addCollege)
        self.ui.addMajorButton.clicked.connect(self.addMajor)
        self.ui.delMajorButton.clicked.connect(self.delMajor)
        self.ui.delCollegeButton.clicked.connect(self.delCollege)
        self.ui.addTrainProgramButton.clicked.connect(self.addTrainProgram)
        self.ui.delTrainProgramButton.clicked.connect(self.delTrainProgram)

    def addCollege(self):
        pass

    def addMajor(self):
        pass

    def delMajor(self):
        pass

    def delCollege(self):
        pass

    def addTrainProgram(self):
        pass

    def delTrainProgram(self):
        pass

