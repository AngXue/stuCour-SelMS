from PyQt5.QtWidgets import QMainWindow

import originalUIFile.userInformWindow as uUserInformWindow


class UserInformWindow(QMainWindow):
    def __init__(self, user, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uUserInformWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('个人信息')
        self.user = user  # 用户对象
        self.slot_init()
        self.showInform()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        pass

    def showInform(self):
        """
        显示个人信息
        stu: id, name, college, major, grade, identify
        tea: id, name, education, degree, collegeID, college, identify
        :return: None
        """
        # 用html格式居中显示所有个人信息
        if self.user.identify == 'student':
            self.ui.showSelfInform.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">学号：%s</span></p></body></html>" % self.user.id +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">姓名：%s</span></p></body></html>" % self.user.name +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">学院：%s</span></p></body></html>" % self.user.college +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">专业：%s</span></p></body></html>" % self.user.major +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">年级：%s</span></p></body></html>" % self.user.grade +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">身份：%s</span></p></body></html>" % self.user.identify
            )
        else:
            self.ui.showSelfInform.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">工号：%s</span></p></body></html>" % self.user.id +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">姓名：%s</span></p></body></html>" % self.user.name +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">学历：%s</span></p></body></html>" % self.user.education +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">学位：%s</span></p></body></html>" % self.user.degree +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">学院：%s</span></p></body></html>" % self.user.college +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">身份：%s</span></p></body></html>" % self.user.identify
            )
