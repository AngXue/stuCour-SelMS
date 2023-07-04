from PyQt5.QtWidgets import QMainWindow

import originalUIFile.login as ulogin
import ui.realizeAdminHome
import ui.realizeStuHome
import ui.realizeTeacherHome


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = ulogin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.slot_init()
        self.setWindowTitle('学生选课管理系统')

    def slot_init(self):
        """
        槽函数初始化
        :return:
        """
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.loginPasswdInput.setEchoMode(2)  # 设置密码输入框为密码模式
        self.ui.loginNameInput.returnPressed.connect(self.login)
        self.ui.loginPasswdInput.returnPressed.connect(self.login)

    def clearPlaceholderText(self):
        """
        清空提示信息，恢复输入框颜色
        :return: None
        """
        self.ui.loginNameInput.setPlaceholderText('')
        self.ui.loginPasswdInput.setPlaceholderText('')
        self.ui.loginNameInput.setStyleSheet("color:black")
        self.ui.loginPasswdInput.setStyleSheet("color:black")

    def login(self):
        """
        登录按钮槽函数
        :return: None
        """

        # 从输入框获取用户名和密码
        userName = self.ui.loginNameInput.text()
        userPasswd = self.ui.loginPasswdInput.text()
        # userInform = llogin.login(userName, userPasswd)
        # [True/False, id/0,'admin'/'student'/'teacher'/'wrong']
        # userInform = [True, 1, 'admin']
        userInform = [True, 2, 'student']
        # userInform = [True, 1, 'teacher']
        # userInform = [False, 0, 'wrong']
        if userInform[0]:
            self.hide()
            if userInform[2] == 'student':
                self.stuHome = ui.realizeStuHome.StuHome(userInform)
                self.stuHome.show()
            elif userInform[2] == 'admin':
                self.adminHome = ui.realizeAdminHome.AdminHomeWindow(userInform)
                self.adminHome.show()
            elif userInform[2] == 'teacher':
                self.teacherHome = ui.realizeTeacherHome.TeacherHomeWindow(userInform)
                self.teacherHome.show()
        else:
            # 清空输入框，设置提示信息
            self.ui.loginNameInput.clear()
            self.ui.loginPasswdInput.clear()
            self.ui.loginNameInput.setFocus()
            self.ui.loginNameInput.setPlaceholderText('用户名或密码错误')
            self.ui.loginPasswdInput.setPlaceholderText('用户名或密码错误')
            self.ui.loginNameInput.setStyleSheet("color:red")
            self.ui.loginPasswdInput.setStyleSheet("color:red")
            # 当用户再次输入时，清空提示信息，恢复输入框颜色
            self.ui.loginNameInput.textChanged.connect(self.clearPlaceholderText)
            self.ui.loginPasswdInput.textChanged.connect(self.clearPlaceholderText)
