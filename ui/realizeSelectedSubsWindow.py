from PyQt5.QtWidgets import QMainWindow

import originalUIFile.selectedSubsWindow as uSelectedSubsWindow


class SelectedSubsWindow(QMainWindow):
    def __init__(self, student, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uSelectedSubsWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('已选课程')
        self.student = student  # 学生对象
        self.slot_init()
        # 用户一进入主界面就显示可选课程
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
        pass
