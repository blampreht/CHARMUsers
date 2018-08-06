# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharmUsers.ui'
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

class Ui_CharmUsers(object):
    def setupUi(self, CharmUsers):
        CharmUsers.setObjectName(_fromUtf8("CharmUsers"))
        CharmUsers.resize(650, 480)
        self.centralwidget = QtGui.QWidget(CharmUsers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gbKTC = QtGui.QGroupBox(self.centralwidget)
        self.gbKTC.setGeometry(QtCore.QRect(10, 40, 290, 140))
        self.gbKTC.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}"))
        self.gbKTC.setObjectName(_fromUtf8("gbKTC"))
        self.KTCProd = QtGui.QCheckBox(self.gbKTC)
        self.KTCProd.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.KTCProd.setObjectName(_fromUtf8("KTCProd"))
        self.KTCAcceptance = QtGui.QCheckBox(self.gbKTC)
        self.KTCAcceptance.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.KTCAcceptance.setObjectName(_fromUtf8("KTCAcceptance"))
        self.KTCTraining = QtGui.QCheckBox(self.gbKTC)
        self.KTCTraining.setGeometry(QtCore.QRect(150, 60, 93, 20))
        self.KTCTraining.setObjectName(_fromUtf8("KTCTraining"))
        self.KTCStaging = QtGui.QCheckBox(self.gbKTC)
        self.KTCStaging.setGeometry(QtCore.QRect(150, 30, 121, 20))
        self.KTCStaging.setObjectName(_fromUtf8("KTCStaging"))
        self.KTCJump = QtGui.QCheckBox(self.gbKTC)
        self.KTCJump.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.KTCJump.setObjectName(_fromUtf8("KTCJump"))
        self.lblEnvs01 = QtGui.QLabel(self.centralwidget)
        self.lblEnvs01.setGeometry(QtCore.QRect(20, 10, 441, 16))
        self.lblEnvs01.setObjectName(_fromUtf8("lblEnvs01"))
        self.gbCGI = QtGui.QGroupBox(self.centralwidget)
        self.gbCGI.setGeometry(QtCore.QRect(340, 40, 290, 140))
        self.gbCGI.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}"))
        self.gbCGI.setObjectName(_fromUtf8("gbCGI"))
        self.CGIProd = QtGui.QCheckBox(self.gbCGI)
        self.CGIProd.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.CGIProd.setObjectName(_fromUtf8("CGIProd"))
        self.CGIAcceptance = QtGui.QCheckBox(self.gbCGI)
        self.CGIAcceptance.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.CGIAcceptance.setObjectName(_fromUtf8("CGIAcceptance"))
        self.CGITraining = QtGui.QCheckBox(self.gbCGI)
        self.CGITraining.setGeometry(QtCore.QRect(150, 60, 93, 20))
        self.CGITraining.setObjectName(_fromUtf8("CGITraining"))
        self.CGIStaging = QtGui.QCheckBox(self.gbCGI)
        self.CGIStaging.setGeometry(QtCore.QRect(150, 30, 121, 20))
        self.CGIStaging.setObjectName(_fromUtf8("CGIStaging"))
        self.CGIJump = QtGui.QCheckBox(self.gbCGI)
        self.CGIJump.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.CGIJump.setObjectName(_fromUtf8("CGIJump"))
        self.gbOthers = QtGui.QGroupBox(self.centralwidget)
        self.gbOthers.setGeometry(QtCore.QRect(10, 200, 290, 110))
        self.gbOthers.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}"))
        self.gbOthers.setObjectName(_fromUtf8("gbOthers"))
        self.Sim = QtGui.QCheckBox(self.gbOthers)
        self.Sim.setGeometry(QtCore.QRect(20, 30, 121, 20))
        self.Sim.setObjectName(_fromUtf8("Sim"))
        self.NFS = QtGui.QCheckBox(self.gbOthers)
        self.NFS.setGeometry(QtCore.QRect(20, 60, 121, 20))
        self.NFS.setObjectName(_fromUtf8("NFS"))
        self.gbMGMT = QtGui.QGroupBox(self.centralwidget)
        self.gbMGMT.setGeometry(QtCore.QRect(340, 200, 290, 110))
        self.gbMGMT.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}"))
        self.gbMGMT.setObjectName(_fromUtf8("gbMGMT"))
        self.MGMTJump = QtGui.QCheckBox(self.gbMGMT)
        self.MGMTJump.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.MGMTJump.setObjectName(_fromUtf8("MGMTJump"))
        self.pbCrtScript = QtGui.QPushButton(self.centralwidget)
        self.pbCrtScript.setGeometry(QtCore.QRect(530, 320, 101, 31))
        self.pbCrtScript.setObjectName(_fromUtf8("pbCrtScript"))
        self.pbDeploy = QtGui.QPushButton(self.centralwidget)
        self.pbDeploy.setGeometry(QtCore.QRect(530, 380, 101, 31))
        self.pbDeploy.setObjectName(_fromUtf8("pbDeploy"))
        self.lblCrtScr = QtGui.QLabel(self.centralwidget)
        self.lblCrtScr.setGeometry(QtCore.QRect(10, 330, 91, 16))
        self.lblCrtScr.setObjectName(_fromUtf8("lblCrtScr"))
        self.leScrName = QtGui.QLineEdit(self.centralwidget)
        self.leScrName.setGeometry(QtCore.QRect(110, 320, 300, 29))
        self.leScrName.setObjectName(_fromUtf8("leScrName"))
        self.lblEnd = QtGui.QLabel(self.centralwidget)
        self.lblEnd.setGeometry(QtCore.QRect(415, 330, 64, 15))
        self.lblEnd.setObjectName(_fromUtf8("lblEnd"))
        CharmUsers.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CharmUsers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_File_2 = QtGui.QMenu(self.menubar)
        self.menu_File_2.setObjectName(_fromUtf8("menu_File_2"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        CharmUsers.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CharmUsers)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CharmUsers.setStatusBar(self.statusbar)
        self.action_Preferences = QtGui.QAction(CharmUsers)
        self.action_Preferences.setObjectName(_fromUtf8("action_Preferences"))
        self.action_About = QtGui.QAction(CharmUsers)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.actionE_xit = QtGui.QAction(CharmUsers)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.menu_File.addAction(self.actionE_xit)
        self.menu_File_2.addAction(self.action_Preferences)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_File_2.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(CharmUsers)
        QtCore.QMetaObject.connectSlotsByName(CharmUsers)

    def retranslateUi(self, CharmUsers):
        CharmUsers.setWindowTitle(_translate("CharmUsers", "CHARM Users Manipulation", None))
        self.gbKTC.setTitle(_translate("CharmUsers", "KTC Environments", None))
        self.KTCProd.setText(_translate("CharmUsers", "Production", None))
        self.KTCAcceptance.setText(_translate("CharmUsers", "Acceptance", None))
        self.KTCTraining.setText(_translate("CharmUsers", "Training", None))
        self.KTCStaging.setText(_translate("CharmUsers", "Staging", None))
        self.KTCJump.setText(_translate("CharmUsers", "Jump hosts", None))
        self.lblEnvs01.setText(_translate("CharmUsers", "Choose the environments, where to create/remove/modify users:", None))
        self.gbCGI.setTitle(_translate("CharmUsers", "CGI Environments", None))
        self.CGIProd.setText(_translate("CharmUsers", "Production", None))
        self.CGIAcceptance.setText(_translate("CharmUsers", "Acceptance", None))
        self.CGITraining.setText(_translate("CharmUsers", "Training", None))
        self.CGIStaging.setText(_translate("CharmUsers", "Staging", None))
        self.CGIJump.setText(_translate("CharmUsers", "Jump hosts", None))
        self.gbOthers.setTitle(_translate("CharmUsers", "Other environments", None))
        self.Sim.setText(_translate("CharmUsers", "Simulators", None))
        self.NFS.setText(_translate("CharmUsers", "NFS clusters", None))
        self.gbMGMT.setTitle(_translate("CharmUsers", "Management", None))
        self.MGMTJump.setText(_translate("CharmUsers", "Jump hosts", None))
        self.pbCrtScript.setText(_translate("CharmUsers", "Create script", None))
        self.pbDeploy.setText(_translate("CharmUsers", "Deploy script", None))
        self.lblCrtScr.setText(_translate("CharmUsers", "Script name: ", None))
        self.lblEnd.setText(_translate("CharmUsers", ".sh", None))
        self.menu_File.setTitle(_translate("CharmUsers", "&File", None))
        self.menu_File_2.setTitle(_translate("CharmUsers", "&Edit", None))
        self.menu_Help.setTitle(_translate("CharmUsers", "&Help", None))
        self.action_Preferences.setText(_translate("CharmUsers", "&Preferences", None))
        self.action_About.setText(_translate("CharmUsers", "&About", None))
        self.actionE_xit.setText(_translate("CharmUsers", "E&xit", None))

