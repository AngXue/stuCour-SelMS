# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(846, 663)
        self.feedbackButton = QtWidgets.QPushButton(Dialog)
        self.feedbackButton.setGeometry(QtCore.QRect(610, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.feedbackButton.setFont(font)
        self.feedbackButton.setStyleSheet("font: 14pt \"Agency FB\";")
        self.feedbackButton.setObjectName("feedbackButton")
        self.logOutButton = QtWidgets.QPushButton(Dialog)
        self.logOutButton.setGeometry(QtCore.QRect(710, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("font: 14pt \"Agency FB\";")
        self.logOutButton.setObjectName("logOutButton")
        self.selfInformButton = QtWidgets.QPushButton(Dialog)
        self.selfInformButton.setGeometry(QtCore.QRect(450, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selfInformButton.setFont(font)
        self.selfInformButton.setStyleSheet("font: 14pt \"Agency FB\";")
        self.selfInformButton.setObjectName("selfInformButton")
        self.showTeacherSubsResult = QtWidgets.QTableWidget(Dialog)
        self.showTeacherSubsResult.setGeometry(QtCore.QRect(70, 160, 711, 431))
        self.showTeacherSubsResult.setObjectName("showTeacherSubsResult")
        self.showTeacherSubsResult.setColumnCount(0)
        self.showTeacherSubsResult.setRowCount(0)
        self.teacherSubsPrompt = QtWidgets.QLabel(Dialog)
        self.teacherSubsPrompt.setGeometry(QtCore.QRect(70, 110, 171, 31))
        self.teacherSubsPrompt.setObjectName("teacherSubsPrompt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.feedbackButton.setText(_translate("Dialog", "反馈"))
        self.logOutButton.setText(_translate("Dialog", "登出"))
        self.selfInformButton.setText(_translate("Dialog", "个人信息"))
        self.teacherSubsPrompt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">任课信息：</span></p></body></html>"))
