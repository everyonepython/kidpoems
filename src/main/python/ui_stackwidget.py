# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stackwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from base import context


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 90, 471, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.j5_page = QtWidgets.QWidget()
        self.j5_page.setEnabled(True)
        self.j5_page.setObjectName("j5_page")
        self.j5_01_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_01_pushButton.setGeometry(QtCore.QRect(10, 33, 70, 70))
        self.j5_01_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_01_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_01_pushButton.setFont(font)
        self.j5_01_pushButton.setText("")
        self.j5_01_pushButton.setObjectName("j5_01_pushButton")
        self.j5_02_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_02_pushButton.setGeometry(QtCore.QRect(86, 33, 70, 70))
        self.j5_02_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_02_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_02_pushButton.setFont(font)
        self.j5_02_pushButton.setText("")
        self.j5_02_pushButton.setObjectName("j5_02_pushButton")
        self.j5_03_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_03_pushButton.setGeometry(QtCore.QRect(162, 33, 70, 70))
        self.j5_03_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_03_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_03_pushButton.setFont(font)
        self.j5_03_pushButton.setText("")
        self.j5_03_pushButton.setObjectName("j5_03_pushButton")
        self.j5_04_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_04_pushButton.setGeometry(QtCore.QRect(238, 33, 70, 70))
        self.j5_04_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_04_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_04_pushButton.setFont(font)
        self.j5_04_pushButton.setText("")
        self.j5_04_pushButton.setObjectName("j5_04_pushButton")
        self.j5_05_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_05_pushButton.setGeometry(QtCore.QRect(314, 33, 70, 70))
        self.j5_05_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_05_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_05_pushButton.setFont(font)
        self.j5_05_pushButton.setText("")
        self.j5_05_pushButton.setObjectName("j5_05_pushButton")
        self.j5_07_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_07_pushButton.setGeometry(QtCore.QRect(10, 106, 70, 70))
        self.j5_07_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_07_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_07_pushButton.setFont(font)
        self.j5_07_pushButton.setText("")
        self.j5_07_pushButton.setObjectName("j5_07_pushButton")
        self.j5_09_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_09_pushButton.setGeometry(QtCore.QRect(162, 106, 70, 70))
        self.j5_09_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_09_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_09_pushButton.setFont(font)
        self.j5_09_pushButton.setText("")
        self.j5_09_pushButton.setObjectName("j5_09_pushButton")
        self.j5_11_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_11_pushButton.setGeometry(QtCore.QRect(314, 106, 70, 70))
        self.j5_11_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_11_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_11_pushButton.setFont(font)
        self.j5_11_pushButton.setText("")
        self.j5_11_pushButton.setObjectName("j5_11_pushButton")
        self.j5_08_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_08_pushButton.setGeometry(QtCore.QRect(86, 106, 70, 70))
        self.j5_08_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_08_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_08_pushButton.setFont(font)
        self.j5_08_pushButton.setText("")
        self.j5_08_pushButton.setObjectName("j5_08_pushButton")
        self.j5_10_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_10_pushButton.setGeometry(QtCore.QRect(238, 106, 70, 70))
        self.j5_10_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_10_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_10_pushButton.setFont(font)
        self.j5_10_pushButton.setText("")
        self.j5_10_pushButton.setObjectName("j5_10_pushButton")
        self.j5_13_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_13_pushButton.setGeometry(QtCore.QRect(10, 179, 70, 70))
        self.j5_13_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_13_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_13_pushButton.setFont(font)
        self.j5_13_pushButton.setText("")
        self.j5_13_pushButton.setObjectName("j5_13_pushButton")
        self.j5_15_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_15_pushButton.setGeometry(QtCore.QRect(162, 179, 70, 70))
        self.j5_15_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_15_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_15_pushButton.setFont(font)
        self.j5_15_pushButton.setText("")
        self.j5_15_pushButton.setObjectName("j5_15_pushButton")
        self.j5_17_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_17_pushButton.setGeometry(QtCore.QRect(314, 179, 70, 70))
        self.j5_17_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_17_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_17_pushButton.setFont(font)
        self.j5_17_pushButton.setText("")
        self.j5_17_pushButton.setObjectName("j5_17_pushButton")
        self.j5_14_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_14_pushButton.setGeometry(QtCore.QRect(86, 179, 70, 70))
        self.j5_14_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_14_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_14_pushButton.setFont(font)
        self.j5_14_pushButton.setText("")
        self.j5_14_pushButton.setObjectName("j5_14_pushButton")
        self.j5_16_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_16_pushButton.setGeometry(QtCore.QRect(238, 179, 70, 70))
        self.j5_16_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_16_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_16_pushButton.setFont(font)
        self.j5_16_pushButton.setText("")
        self.j5_16_pushButton.setObjectName("j5_16_pushButton")
        self.j5_19_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_19_pushButton.setGeometry(QtCore.QRect(10, 252, 70, 70))
        self.j5_19_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_19_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_19_pushButton.setFont(font)
        self.j5_19_pushButton.setText("")
        self.j5_19_pushButton.setObjectName("j5_19_pushButton")
        self.j5_21_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_21_pushButton.setGeometry(QtCore.QRect(162, 252, 70, 70))
        self.j5_21_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_21_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_21_pushButton.setFont(font)
        self.j5_21_pushButton.setText("")
        self.j5_21_pushButton.setObjectName("j5_21_pushButton")
        self.j5_23_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_23_pushButton.setGeometry(QtCore.QRect(314, 252, 70, 70))
        self.j5_23_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_23_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_23_pushButton.setFont(font)
        self.j5_23_pushButton.setText("")
        self.j5_23_pushButton.setObjectName("j5_23_pushButton")
        self.j5_20_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_20_pushButton.setGeometry(QtCore.QRect(86, 252, 70, 70))
        self.j5_20_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_20_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_20_pushButton.setFont(font)
        self.j5_20_pushButton.setText("")
        self.j5_20_pushButton.setObjectName("j5_20_pushButton")
        self.j5_22_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_22_pushButton.setGeometry(QtCore.QRect(238, 252, 70, 70))
        self.j5_22_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_22_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_22_pushButton.setFont(font)
        self.j5_22_pushButton.setText("")
        self.j5_22_pushButton.setObjectName("j5_22_pushButton")
        self.j5_18_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_18_pushButton.setGeometry(QtCore.QRect(390, 179, 70, 70))
        self.j5_18_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_18_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_18_pushButton.setFont(font)
        self.j5_18_pushButton.setText("")
        self.j5_18_pushButton.setObjectName("j5_18_pushButton")
        self.j5_24_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_24_pushButton.setGeometry(QtCore.QRect(390, 252, 70, 70))
        self.j5_24_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_24_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_24_pushButton.setFont(font)
        self.j5_24_pushButton.setText("")
        self.j5_24_pushButton.setObjectName("j5_24_pushButton")
        self.j5_12_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_12_pushButton.setGeometry(QtCore.QRect(390, 106, 70, 70))
        self.j5_12_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_12_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_12_pushButton.setFont(font)
        self.j5_12_pushButton.setText("")
        self.j5_12_pushButton.setObjectName("j5_12_pushButton")
        self.j5_06_pushButton = QtWidgets.QPushButton(self.j5_page)
        self.j5_06_pushButton.setGeometry(QtCore.QRect(390, 33, 70, 70))
        self.j5_06_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.j5_06_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j5_06_pushButton.setFont(font)
        self.j5_06_pushButton.setText("")
        self.j5_06_pushButton.setCheckable(False)
        self.j5_06_pushButton.setObjectName("j5_06_pushButton")
        self.stackedWidget.addWidget(self.j5_page)
        self.j7_page = QtWidgets.QWidget()
        self.j7_page.setObjectName("j7_page")
        self.j7_08_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_08_pushButton.setGeometry(QtCore.QRect(405, 31, 65, 65))
        self.j7_08_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_08_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_08_pushButton.setFont(font)
        self.j7_08_pushButton.setText("")
        self.j7_08_pushButton.setCheckable(False)
        self.j7_08_pushButton.setObjectName("j7_08_pushButton")
        self.j7_03_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_03_pushButton.setGeometry(QtCore.QRect(115, 31, 65, 65))
        self.j7_03_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_03_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_03_pushButton.setFont(font)
        self.j7_03_pushButton.setText("")
        self.j7_03_pushButton.setObjectName("j7_03_pushButton")
        self.j7_04_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_04_pushButton.setGeometry(QtCore.QRect(173, 31, 65, 65))
        self.j7_04_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_04_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_04_pushButton.setFont(font)
        self.j7_04_pushButton.setText("")
        self.j7_04_pushButton.setObjectName("j7_04_pushButton")
        self.j7_02_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_02_pushButton.setGeometry(QtCore.QRect(57, 31, 65, 65))
        self.j7_02_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_02_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_02_pushButton.setFont(font)
        self.j7_02_pushButton.setText("")
        self.j7_02_pushButton.setObjectName("j7_02_pushButton")
        self.j7_07_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_07_pushButton.setGeometry(QtCore.QRect(347, 31, 65, 65))
        self.j7_07_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_07_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_07_pushButton.setFont(font)
        self.j7_07_pushButton.setText("")
        self.j7_07_pushButton.setCheckable(False)
        self.j7_07_pushButton.setObjectName("j7_07_pushButton")
        self.j7_05_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_05_pushButton.setGeometry(QtCore.QRect(231, 31, 65, 65))
        self.j7_05_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_05_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_05_pushButton.setFont(font)
        self.j7_05_pushButton.setText("")
        self.j7_05_pushButton.setObjectName("j7_05_pushButton")
        self.j7_06_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_06_pushButton.setGeometry(QtCore.QRect(289, 31, 65, 65))
        self.j7_06_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_06_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_06_pushButton.setFont(font)
        self.j7_06_pushButton.setText("")
        self.j7_06_pushButton.setCheckable(False)
        self.j7_06_pushButton.setObjectName("j7_06_pushButton")
        self.j7_01_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_01_pushButton.setGeometry(QtCore.QRect(-1, 31, 65, 65))
        self.j7_01_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_01_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_01_pushButton.setFont(font)
        self.j7_01_pushButton.setText("")
        self.j7_01_pushButton.setObjectName("j7_01_pushButton")
        self.j7_16_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_16_pushButton.setGeometry(QtCore.QRect(405, 109, 65, 65))
        self.j7_16_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_16_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_16_pushButton.setFont(font)
        self.j7_16_pushButton.setText("")
        self.j7_16_pushButton.setCheckable(False)
        self.j7_16_pushButton.setObjectName("j7_16_pushButton")
        self.j7_12_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_12_pushButton.setGeometry(QtCore.QRect(173, 109, 65, 65))
        self.j7_12_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_12_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_12_pushButton.setFont(font)
        self.j7_12_pushButton.setText("")
        self.j7_12_pushButton.setObjectName("j7_12_pushButton")
        self.j7_09_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_09_pushButton.setGeometry(QtCore.QRect(-1, 109, 65, 65))
        self.j7_09_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_09_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_09_pushButton.setFont(font)
        self.j7_09_pushButton.setText("")
        self.j7_09_pushButton.setObjectName("j7_09_pushButton")
        self.j7_15_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_15_pushButton.setGeometry(QtCore.QRect(347, 109, 65, 65))
        self.j7_15_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_15_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_15_pushButton.setFont(font)
        self.j7_15_pushButton.setText("")
        self.j7_15_pushButton.setCheckable(False)
        self.j7_15_pushButton.setObjectName("j7_15_pushButton")
        self.j7_10_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_10_pushButton.setGeometry(QtCore.QRect(57, 109, 65, 65))
        self.j7_10_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_10_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_10_pushButton.setFont(font)
        self.j7_10_pushButton.setText("")
        self.j7_10_pushButton.setObjectName("j7_10_pushButton")
        self.j7_14_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_14_pushButton.setGeometry(QtCore.QRect(289, 109, 65, 65))
        self.j7_14_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_14_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_14_pushButton.setFont(font)
        self.j7_14_pushButton.setText("")
        self.j7_14_pushButton.setObjectName("j7_14_pushButton")
        self.j7_11_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_11_pushButton.setGeometry(QtCore.QRect(115, 109, 65, 65))
        self.j7_11_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_11_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_11_pushButton.setFont(font)
        self.j7_11_pushButton.setText("")
        self.j7_11_pushButton.setObjectName("j7_11_pushButton")
        self.j7_13_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_13_pushButton.setGeometry(QtCore.QRect(231, 109, 65, 65))
        self.j7_13_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_13_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_13_pushButton.setFont(font)
        self.j7_13_pushButton.setText("")
        self.j7_13_pushButton.setObjectName("j7_13_pushButton")
        self.j7_24_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_24_pushButton.setGeometry(QtCore.QRect(404, 184, 65, 65))
        self.j7_24_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_24_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_24_pushButton.setFont(font)
        self.j7_24_pushButton.setText("")
        self.j7_24_pushButton.setCheckable(False)
        self.j7_24_pushButton.setObjectName("j7_24_pushButton")
        self.j7_17_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_17_pushButton.setGeometry(QtCore.QRect(-2, 184, 65, 65))
        self.j7_17_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_17_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_17_pushButton.setFont(font)
        self.j7_17_pushButton.setText("")
        self.j7_17_pushButton.setObjectName("j7_17_pushButton")
        self.j7_19_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_19_pushButton.setGeometry(QtCore.QRect(114, 184, 65, 65))
        self.j7_19_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_19_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_19_pushButton.setFont(font)
        self.j7_19_pushButton.setText("")
        self.j7_19_pushButton.setObjectName("j7_19_pushButton")
        self.j7_21_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_21_pushButton.setGeometry(QtCore.QRect(230, 184, 65, 65))
        self.j7_21_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_21_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_21_pushButton.setFont(font)
        self.j7_21_pushButton.setText("")
        self.j7_21_pushButton.setObjectName("j7_21_pushButton")
        self.j7_23_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_23_pushButton.setGeometry(QtCore.QRect(346, 184, 65, 65))
        self.j7_23_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_23_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_23_pushButton.setFont(font)
        self.j7_23_pushButton.setText("")
        self.j7_23_pushButton.setCheckable(False)
        self.j7_23_pushButton.setObjectName("j7_23_pushButton")
        self.j7_18_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_18_pushButton.setGeometry(QtCore.QRect(56, 184, 65, 65))
        self.j7_18_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_18_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_18_pushButton.setFont(font)
        self.j7_18_pushButton.setText("")
        self.j7_18_pushButton.setObjectName("j7_18_pushButton")
        self.j7_22_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_22_pushButton.setGeometry(QtCore.QRect(288, 184, 65, 65))
        self.j7_22_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_22_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_22_pushButton.setFont(font)
        self.j7_22_pushButton.setText("")
        self.j7_22_pushButton.setObjectName("j7_22_pushButton")
        self.j7_20_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_20_pushButton.setGeometry(QtCore.QRect(172, 184, 65, 65))
        self.j7_20_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_20_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_20_pushButton.setFont(font)
        self.j7_20_pushButton.setText("")
        self.j7_20_pushButton.setObjectName("j7_20_pushButton")
        self.j7_26_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_26_pushButton.setGeometry(QtCore.QRect(56, 260, 65, 65))
        self.j7_26_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_26_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_26_pushButton.setFont(font)
        self.j7_26_pushButton.setText("")
        self.j7_26_pushButton.setObjectName("j7_26_pushButton")
        self.j7_28_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_28_pushButton.setGeometry(QtCore.QRect(172, 260, 65, 65))
        self.j7_28_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_28_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_28_pushButton.setFont(font)
        self.j7_28_pushButton.setText("")
        self.j7_28_pushButton.setObjectName("j7_28_pushButton")
        self.j7_31_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_31_pushButton.setGeometry(QtCore.QRect(346, 260, 65, 65))
        self.j7_31_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_31_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_31_pushButton.setFont(font)
        self.j7_31_pushButton.setText("")
        self.j7_31_pushButton.setCheckable(False)
        self.j7_31_pushButton.setObjectName("j7_31_pushButton")
        self.j7_25_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_25_pushButton.setGeometry(QtCore.QRect(-2, 260, 65, 65))
        self.j7_25_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_25_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_25_pushButton.setFont(font)
        self.j7_25_pushButton.setText("")
        self.j7_25_pushButton.setObjectName("j7_25_pushButton")
        self.j7_29_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_29_pushButton.setGeometry(QtCore.QRect(230, 260, 65, 65))
        self.j7_29_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_29_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_29_pushButton.setFont(font)
        self.j7_29_pushButton.setText("")
        self.j7_29_pushButton.setObjectName("j7_29_pushButton")
        self.j7_32_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_32_pushButton.setGeometry(QtCore.QRect(404, 260, 65, 65))
        self.j7_32_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_32_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_32_pushButton.setFont(font)
        self.j7_32_pushButton.setText("")
        self.j7_32_pushButton.setCheckable(False)
        self.j7_32_pushButton.setObjectName("j7_32_pushButton")
        self.j7_27_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_27_pushButton.setGeometry(QtCore.QRect(114, 260, 65, 65))
        self.j7_27_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_27_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_27_pushButton.setFont(font)
        self.j7_27_pushButton.setText("")
        self.j7_27_pushButton.setObjectName("j7_27_pushButton")
        self.j7_30_pushButton = QtWidgets.QPushButton(self.j7_page)
        self.j7_30_pushButton.setGeometry(QtCore.QRect(288, 260, 65, 65))
        self.j7_30_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.j7_30_pushButton.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.j7_30_pushButton.setFont(font)
        self.j7_30_pushButton.setText("")
        self.j7_30_pushButton.setObjectName("j7_30_pushButton")
        self.stackedWidget.addWidget(self.j7_page)
        self.l5_page = QtWidgets.QWidget()
        self.l5_page.setObjectName("l5_page")
        self.label_3 = QtWidgets.QLabel(self.l5_page)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 59, 16))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.l5_page)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.chs_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.chs_checkBox.setGeometry(QtCore.QRect(30, 390, 81, 41))
        self.chs_checkBox.setObjectName("chs_checkBox")
        self.title_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.title_pushButton.setEnabled(True)
        self.title_pushButton.setGeometry(QtCore.QRect(168, -4, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.title_pushButton.setFont(font)
        self.title_pushButton.setText("")
        self.title_pushButton.setAutoDefault(False)
        self.title_pushButton.setDefault(False)
        self.title_pushButton.setFlat(True)
        self.title_pushButton.setObjectName("title_pushButton")
        self.author_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.author_pushButton.setGeometry(QtCore.QRect(168, 60, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.author_pushButton.setFont(font)
        self.author_pushButton.setText("")
        self.author_pushButton.setFlat(True)
        self.author_pushButton.setObjectName("author_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "五言律诗"))
        self.chs_checkBox.setText(_translate("MainWindow", "简体版本"))
