# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Preferences.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(400, 200)
        Preferences.setMinimumSize(QtCore.QSize(400, 200))
        Preferences.setMaximumSize(QtCore.QSize(400, 200))
        self.lblPrefText = QtGui.QLabel(Preferences)
        self.lblPrefText.setGeometry(QtCore.QRect(20, 10, 271, 16))
        self.lblPrefText.setObjectName(_fromUtf8("lblPrefText"))
        self.lblUsername = QtGui.QLabel(Preferences)
        self.lblUsername.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.lblUsername.setObjectName(_fromUtf8("lblUsername"))
        self.lblPassword = QtGui.QLabel(Preferences)
        self.lblPassword.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.leCHARMUsername = QtGui.QLineEdit(Preferences)
        self.leCHARMUsername.setGeometry(QtCore.QRect(100, 40, 150, 29))
        self.leCHARMUsername.setObjectName(_fromUtf8("leCHARMUsername"))
        self.leCHARMPassword = QtGui.QLineEdit(Preferences)
        self.leCHARMPassword.setGeometry(QtCore.QRect(100, 80, 150, 29))
        self.leCHARMPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.leCHARMPassword.setObjectName(_fromUtf8("leCHARMPassword"))
        self.pbPrefOK = QtGui.QPushButton(Preferences)
        self.pbPrefOK.setGeometry(QtCore.QRect(180, 140, 91, 31))
        self.pbPrefOK.setObjectName(_fromUtf8("pbPrefOK"))
        self.pbPrefCancel = QtGui.QPushButton(Preferences)
        self.pbPrefCancel.setGeometry(QtCore.QRect(290, 140, 91, 31))
        self.pbPrefCancel.setObjectName(_fromUtf8("pbPrefCancel"))

        self.retranslateUi(Preferences)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Dialog", None))
        self.lblPrefText.setText(_translate("Preferences", "Mandatory settings for script generation:", None))
        self.lblUsername.setText(_translate("Preferences", "Username: ", None))
        self.lblPassword.setText(_translate("Preferences", "Password:", None))
        self.pbPrefOK.setText(_translate("Preferences", "OK", None))
        self.pbPrefCancel.setText(_translate("Preferences", "Cancel", None))

