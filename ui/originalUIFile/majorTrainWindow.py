# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'majorTrainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 506)
        Dialog.setMinimumSize(QtCore.QSize(700, 506))
        Dialog.setMaximumSize(QtCore.QSize(700, 506))
        self.topPrompt = QtWidgets.QLabel(Dialog)
        self.topPrompt.setGeometry(QtCore.QRect(310, 10, 91, 20))
        self.topPrompt.setObjectName("topPrompt")
        self.showMajorTrainResult = QtWidgets.QTableWidget(Dialog)
        self.showMajorTrainResult.setGeometry(QtCore.QRect(5, 41, 691, 451))
        self.showMajorTrainResult.setObjectName("showMajorTrainResult")
        self.showMajorTrainResult.setColumnCount(0)
        self.showMajorTrainResult.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.topPrompt.setText(_translate("Dialog", "专业培养方案"))
