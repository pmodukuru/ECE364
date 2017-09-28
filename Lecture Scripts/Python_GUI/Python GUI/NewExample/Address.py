# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Address.ui'
#
# Created: Mon Mar 20 12:05:07 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(523, 429)
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.txtName = QtGui.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(160, 40, 291, 27))
        self.txtName.setObjectName("txtName")
        self.lblName = QtGui.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(70, 40, 62, 17))
        self.lblName.setObjectName("lblName")
        self.cboValues = QtGui.QComboBox(self.centralwidget)
        self.cboValues.setGeometry(QtCore.QRect(160, 90, 291, 27))
        self.cboValues.setObjectName("cboValues")
        self.cboValues.addItem("")
        self.cboValues.addItem("")
        self.cboValues.addItem("")
        self.lblLocation = QtGui.QLabel(self.centralwidget)
        self.lblLocation.setGeometry(QtCore.QRect(60, 90, 62, 17))
        self.lblLocation.setObjectName("lblLocation")
        self.btnDisplay = QtGui.QPushButton(self.centralwidget)
        self.btnDisplay.setGeometry(QtCore.QRect(180, 160, 92, 27))
        self.btnDisplay.setObjectName("btnDisplay")
        self.txtDisplay = QtGui.QLineEdit(self.centralwidget)
        self.txtDisplay.setGeometry(QtCore.QRect(50, 230, 401, 41))
        self.txtDisplay.setReadOnly(True)
        self.txtDisplay.setObjectName("txtDisplay")
        self.txtRichDisplay = QtGui.QTextEdit(self.centralwidget)
        self.txtRichDisplay.setGeometry(QtCore.QRect(50, 280, 401, 61))
        self.txtRichDisplay.setObjectName("txtRichDisplay")
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 25))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("Window", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cboValues.setItemText(0, QtGui.QApplication.translate("Window", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.cboValues.setItemText(1, QtGui.QApplication.translate("Window", "Work", None, QtGui.QApplication.UnicodeUTF8))
        self.cboValues.setItemText(2, QtGui.QApplication.translate("Window", "Co-Rec", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLocation.setText(QtGui.QApplication.translate("Window", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDisplay.setText(QtGui.QApplication.translate("Window", "Display", None, QtGui.QApplication.UnicodeUTF8))

