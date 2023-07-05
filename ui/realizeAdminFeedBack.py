from PyQt5.QtWidgets import QMainWindow

import originalUIFile.adminFeedBack as uadminFeedBack


class AdminFeedBackWindow(QMainWindow):
    def __init__(self, admin, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uadminFeedBack.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()
        self.admin = admin  # 管理员对象
        self.setWindowTitle('管理员反馈信息界面')
        self.showFeedBack()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        pass

    def showFeedBack(self):
        """
        显示反馈信息
        :return: None
        """
        message = self.admin.viewmessage()
        # message (('Something'), ('Something'), ('Something'))
        # 将反馈信息显示在self.ui.listWidget中
        for i in range(len(message)):
            self.ui.listWidget.addItem(message[i][2])

