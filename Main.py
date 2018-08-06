#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################
#
# CHARM Users Manipulation: Main class
#
#
# Author: blaz.lampreht@gmail.com
#
############################################

#imports

import sys, os
from PyQt4 import QtCore, QtGui
from CharmUsers import Ui_CharmUsers
from Preferences import Ui_Preferences
import WorkingClass
import Defines

## Globals ##

environments = {
    "KTCProd":False,
    "KTCStaging":False,
    "KTCAcceptance":False,
    "KTCTraining":False,
    "KTCJump":False,
    "CGIProd":False,
    "CGIAcceptance":False,
    "CGIStaging":False,
    "CGITraining":False,
    "CGIJump":False,
    "Sim":False,
    "NFS":False,
    "MGMTJump":False
}

vm_groups = {
    "KTCProd":"",
    "KTCStaging":"",
    "KTCAcceptance":"",
    "KTCTraining":"",
    "KTCJump":"",
    "CGIProd":"",
    "CGIAcceptance":"",
    "CGIStaging":"",
    "CGITraining":"",
    "CGIJump":"",
    "Sim":"",
    "NFS":"",
    "MGMTJump":""
}

paths = []


#############

## Class ##

class StartQT4(QtGui.QMainWindow):
    ## Main init function

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CharmUsers()
        self.ui.setupUi(self)

        # Move to center screen:

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # A few globals

        self.CHARMUsername = ""
        self.CHARMPassword = ""
        self.jumphost      = ""
        self.credentials   = False

        ###############

        # Setup the Preferences window

        self.dialog = QtGui.QDialog()
        self.dialog.ui = Ui_Preferences()
        self.dialog.ui.setupUi(self.dialog)

        #### Signals and slots ####

        # Menu bar

        QtCore.QObject.connect(self.ui.actionE_xit, QtCore.SIGNAL("triggered()"), self.AppExit)
        QtCore.QObject.connect(self.ui.action_Preferences, QtCore.SIGNAL("triggered()"), self.OpenPreferences)

        # Buttons

        QtCore.QObject.connect(self.ui.pbCrtScript, QtCore.SIGNAL("clicked()"), self.CreateScript)
        QtCore.QObject.connect(self.ui.pbDeploy, QtCore.SIGNAL("clicked()"), self.DeployScript)


        # Check boxes

        QtCore.QObject.connect(self.ui.KTCProd, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.KTCStaging, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.KTCAcceptance, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.KTCTraining, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.KTCJump, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.CGIProd, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.CGIAcceptance, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.CGIStaging, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.CGITraining, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.CGIJump, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.Sim, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.NFS, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)
        QtCore.QObject.connect(self.ui.MGMTJump, QtCore.SIGNAL("stateChanged(int)"), self.AddToList)

        # Preferences window

        QtCore.QObject.connect(self.dialog.ui.pbPrefCancel,QtCore.SIGNAL("clicked()"), self.prefCancel)
        QtCore.QObject.connect(self.dialog.ui.pbPrefOK,QtCore.SIGNAL("clicked()"), self.prefOK)

        # initialize

        self.init()

    #### ACTION HANDLERS ###

    ##
    # Exit application
    ##
    def AppExit(self):
        sys.exit(0)


    ##
    # Function to handle Edit -> Preferences
    ##
    def OpenPreferences(self):
        self.dialog.exec_()

    ##
    # Function to handle OK in Preferences
    ##
    def prefOK(self):

        self.CHARMUsername = str(self.dialog.ui.leCHARMUsername.text()).strip()
        self.CHARMPassword = str(self.dialog.ui.leCHARMPassword.text()).strip()

        if (self.CHARMUsername=="" or self.CHARMPassword==""):
            QtGui.QMessageBox.warning(self,"Error","One of the fields (username(password) was left empty. Please fill it out before continuing.")
        else:
            self.credentials = True
            self.dialog.reject()

    ##
    # Function to handle Cancel in Preferences
    ##
    def prefCancel(self):
        self.dialog.ui.leCHARMUsername.setText("")
        self.dialog.ui.leCHARMPassword.setText("")
        self.credentials = False
        self.dialog.reject()

    ##
    # Function that creates a custom script
    ##
    def CreateScript(self):

        global paths
        global environments
        global vm_groups

        retval = Defines.NOT_OK

        wc = WorkingClass.WorkingClass()

        script_name = str(self.ui.leScrName.text())
        script_path = os.path.join(paths[Defines.SCR_PATH],script_name)

        if (not script_path.endswith(".sh")):
            script_path = script_path+".sh"


        if (not self.credentials):
            QtGui.QMessageBox.warning(self,"Error","Please set the credentials under Edit->Preferences before creating the script.")

        elif (not script_name == ""):
            if os.path.exists(script_path):

                reply = QtGui.QMessageBox.question(self,"Question", "The script with the selected name already exists in the configured path. Would you like to overwrite it ?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

                if (reply == QtGui.QMessageBox.No):
                    self.ui.leScrName.setText("")
                else:
                    retval = wc.createScript(script_path, environments, vm_groups, paths[Defines.USR_PATH],self.CHARMUsername,self.CHARMPassword)
                    if (retval==Defines.ALL_OK):
                        QtGui.QMessageBox.information(self,"Success", "The script has been created.")
                    else:
                        QtGui.QMessageBox.warning(self,"Problem !", "There has been a problem creating the script.")

            else:
                retval = wc.createScript(script_path, environments, vm_groups, paths[Defines.USR_PATH],self.CHARMUsername,self.CHARMPassword)
                if (retval==Defines.ALL_OK):
                    QtGui.QMessageBox.information(self,"Success", "The script has been created.")
                else:
                    QtGui.QMessageBox.warning(self,"Problem !", "There has been a problem creating the script.")

        else:
            QtGui.QMessageBox.critical(self,"Error","No script name has been provided. Aborting ...")



    def DeployScript(self):

        wc = WorkingClass.WorkingClass()
        retval = Defines.ALL_OK
        script_name = str(self.ui.leScrName.text()).strip()

        if (not script_name.endswith(".sh")):
            script_name = script_name+".sh"

        script_path = os.path.join(paths[Defines.SCR_PATH],script_name)
        wrapper_script = os.path.join(paths[Defines.SCR_PATH],"wrapper_"+script_name)

        retval = wc.deployScript(script_path, wrapper_script, script_name, self.CHARMUsername, paths[Defines.JMP_HOST])

        if (retval==Defines.ALL_OK):
            QtGui.QMessageBox.information(self,"Success", "The script has been successfully deployed.")
        else:
            QtGui.QMessageBox.warning(self,"Problem !", "There has been a problem deploying the script.")


    def AddToList(self):

        sending_box = self.sender()

        if (sending_box.isChecked()):
            environments[str(sending_box.objectName()).strip()] = True
        else:
            environments[str(sending_box.objectName()).strip()] = False


    ##
    # Initialization
    ##
    def init(self):

        global paths

        wc = WorkingClass.WorkingClass()
        conf_file = os.path.join(os.getcwd(),"config")

        if not os.path.isfile(conf_file):
            QtGui.QMessageBox.warning(self,"Error", "The configuration file does not exist. Create a 'config' file and place it in your CWD.\nExiting ...")
            sys.exit(1)
        else:
            paths = wc.getPaths(conf_file)

            if not os.path.exists(paths[Defines.SCR_PATH]):
                QtGui.QMessageBox.warning(self,"Error", "The configuration file does not contain a valid script path. Correct the path and try again.\nExiting ...")
                sys.exit(1)

            if not os.path.exists(paths[Defines.ENV_PATH]):
                QtGui.QMessageBox.warning(self,"Error", "The configuration file does not contain a valid environment file path. Correct the path and try again.\nExiting ...")
                sys.exit(1)

            if not os.path.exists(paths[Defines.USR_PATH]):
                QtGui.QMessageBox.warning(self,"Error", "The configuration file does not contain a valid users file path. Correct the path and try again.\nExiting ...")
                sys.exit(1)

            wc.prepare_vm_groups(paths[Defines.ENV_PATH],vm_groups)


## Main function - application start

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
