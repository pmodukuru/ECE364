# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SomeFile.ui'
#
# Created: Mon Mar 20 11:55:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 339)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtFirstName = QtGui.QLineEdit(self.centralwidget)
        self.txtFirstName.setGeometry(QtCore.QRect(150, 40, 381, 51))
        self.txtFirstName.setObjectName("txtFirstName")
        self.lblFirstName = QtGui.QLabel(self.centralwidget)
        self.lblFirstName.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.lblFirstName.setObjectName("lblFirstName")
        self.lblTarget = QtGui.QLabel(self.centralwidget)
        self.lblTarget.setGeometry(QtCore.QRect(150, 220, 381, 51))
        self.lblTarget.setText("")
        self.lblTarget.setObjectName("lblTarget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.txtFirstName, QtCore.SIGNAL("textChanged(QString)"), self.lblTarget.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFirstName.setText(QtGui.QApplication.translate("MainWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))

