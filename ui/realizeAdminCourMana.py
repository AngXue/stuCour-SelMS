from PyQt5.QtWidgets import QMainWindow

import originalUIFile.adminCourseManage as uadminCourseManage


class AdminCourseManageWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AdminCourseManageWindow, self).__init__(parent)
        self.ui = uadminCourseManage.Ui_Dialog()
        self.ui.setupUi(self)
        self.slot_init()

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.uploadCourseButton.clicked.connect(self.uploadCourse)
        self.ui.deleteCourseButton.clicked.connect(self.deleteCourse)
        self.ui.deleteCourseStuButton.clicked.connect(self.deleteCourseStu)
        self.ui.deleteCourseteacherButton.clicked.connect(self.deleteCourseteacher)
        self.ui.courseSearchButton.clicked.connect(self.courseSearch)

    def uploadCourse(self):
        """
        上传课程
        :return:
        """
        pass

    def deleteCourse(self):
        """
        删除课程
        :return:
        """
        pass

    def deleteCourseStu(self):
        """
        删除课程学生
        :return:
        """
        pass

    def deleteCourseteacher(self):
        """
        删除课程教师
        :return:
        """
        pass

    def courseSearch(self):
        """
        课程查询
        :return:
        """
        pass
