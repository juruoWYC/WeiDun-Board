# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        font = QtGui.QFont()
        font.setFamily("黑体")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 30, 430, 520))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 140, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.num1_1 = QtWidgets.QLCDNumber(self.groupBox)
        self.num1_1.setGeometry(QtCore.QRect(180, 75, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.num1_1.setFont(font)
        self.num1_1.setSmallDecimalPoint(False)
        self.num1_1.setDigitCount(5)
        self.num1_1.setMode(QtWidgets.QLCDNumber.Dec)
        self.num1_1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.num1_1.setProperty("value", 0.0)
        self.num1_1.setObjectName("num1_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 140, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 370, 140, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.num1_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.num1_2.setGeometry(QtCore.QRect(180, 225, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.num1_2.setFont(font)
        self.num1_2.setSmallDecimalPoint(False)
        self.num1_2.setDigitCount(5)
        self.num1_2.setMode(QtWidgets.QLCDNumber.Dec)
        self.num1_2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.num1_2.setProperty("value", 0.0)
        self.num1_2.setObjectName("num1_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(330, 200, 200, 120))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(40)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.num1_3 = QtWidgets.QLCDNumber(self.groupBox)
        self.num1_3.setGeometry(QtCore.QRect(180, 375, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.num1_3.setFont(font)
        self.num1_3.setSmallDecimalPoint(False)
        self.num1_3.setDigitCount(5)
        self.num1_3.setMode(QtWidgets.QLCDNumber.Dec)
        self.num1_3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.num1_3.setProperty("value", 0.0)
        self.num1_3.setObjectName("num1_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(330, 350, 200, 120))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(340, 50, 200, 120))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.main_pic = QtWidgets.QLabel(self.centralwidget)
        self.main_pic.setGeometry(QtCore.QRect(910, 510, 80, 60))
        self.main_pic.setText("")
        self.main_pic.setObjectName("main_pic")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "薇盾监控面板"))
        self.label.setText(_translate("MainWindow", "空气湿度:"))
        self.label_2.setText(_translate("MainWindow", "空气温度:"))
        self.label_3.setText(_translate("MainWindow", "光照强度："))
        self.label_5.setText(_translate("MainWindow", "℃"))
        self.label_6.setText(_translate("MainWindow", "勒克斯"))
        self.label_7.setText(_translate("MainWindow", "%"))
