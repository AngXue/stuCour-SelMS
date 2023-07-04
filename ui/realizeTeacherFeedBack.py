from PyQt5.QtWidgets import QMainWindow

import originalUIFile.teacherFeedback as uTeacherFeedback


class TeacherFeedbackWindow(QMainWindow):
    def __init__(self, teacher, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = uTeacherFeedback.Ui_Dialog()
        self.ui.setupUi(self)
        self.teacher = teacher
        self.slot_init()
        self.setWindowTitle('教师反馈界面')

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.submitButton.clicked.connect(self.submit)
        # 初始化self.ui.messageTextEdit内容为教师ID和姓名
        self.ui.messageTextEdit.setText(
            '教师ID: ' + str(self.teacher.id) + '\n' + '教师姓名: ' + self.teacher.name + '\n')

    def submit(self):
        """
        提交反馈
        :return: None
        """
        # 获取反馈信息
        feedback = self.ui.messageTextEdit.toPlainText()
        # self.teacher.feedback(feedback) TODO: 调用教师反馈函数
