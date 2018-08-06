############################################
#
# WorkingClass: A class that holds all
#               main worker functions
#
# Author: blaz.lampreht@gmail.com
#
############################################

import os
from PyQt4 import QtGui
import Defines
import subprocess

##
# Class that contains worker functions
##
class WorkingClass(object):


    ##
    # Constructor
    ##

    def __init__(self):
        nothing=0



    #### END OF CONSTRUCTOR ####


    ##
    # Function that reads the config file
    # and parses it
    # @return: Returns two paths:
    # - script path
    # - environments file path
    ##
    def getPaths(self, config_path):

        fh = open(config_path, "r")
        scr_path = 'None'
        env_path = 'None'
        usr_path = 'None'
        paths    = []

        for line in fh:

            if line.startswith('#'):
                continue

            elif line.startswith('scr_path'):
                ln=line.split('=')
                scr_path=ln[1].strip()
            elif line.startswith('env_path'):
                ln=line.split('=')
                env_path=ln[1].strip()
            elif line.startswith('usr_path'):
                ln=line.split('=')
                usr_path=ln[1].strip()
            elif line.startswith('jump_host'):
                ln=line.split('=')
                jump_host=ln[1].strip()


        paths.append(scr_path)
        paths.append(env_path)
        paths.append(usr_path)
        paths.append(jump_host)

        fh.close()

        return paths

    #### END OF FUNCTION ####

    ##
    #
    # Procedure reads the environments file and
    # prepares the global array of VMs for each ENV group
    #
    ##
    def prepare_vm_groups(self,env_path,vm_groups):

        fh = open(env_path, "r")

        # Create a list of environments

        grouplist = []

        for key in vm_groups:
            grouplist.append(key)

        ###############################

        # Go through environments
        # and save VMs to a vm_group list

        j = ""
        m = ""

        for line in fh:

            if line.startswith('#'):
                continue

            ln = line.split('=')

            if ln[0] in grouplist:
                vm_groups[str(ln[0]).strip()] = str(ln[1]).strip()


        ###############################
        fh.close()

    #### END OF FUNCTION ####

    ##
    # This is a helper function for the createScript function
    ##
    def createCommand(self,params):

        username = params[0].strip()
        operation = ""
        add2group = params[2].strip()

        if (params[1].strip()=="add"):
            operation = "sudo /sbin/useradd -m " + username + ";chage -M 99999 " + username
        elif (params[1].strip()=="rm"):
            operation = "sudo /sbin/userdel -rf " + username
        elif (params[1].strip()=="mod"):
            if not add2group=="none":
                operation = "sudo /sbin/usermod -aG " + add2group + " " + username

        return operation

    #### END OF FUNCTION ####

    ##
    # Another helper function that creates custom commands
    ##

    def customCommand(self,params):

        username = params[0].strip()
        customcmd = params[1].strip() + " " + username

        return customcmd

    #### END OF FUNCTION ####

    ##
    # Functions takes all information and creates a script
    ##
    def createScript(self, script_path, environments, vm_groups, users_path, uname, passwd):

        retval = Defines.ALL_OK

        commands = []

        user_fh = open(users_path,"r")

        ### Prepare commands ###

        script_fh = open(script_path,"w")

        for line in user_fh:

            if line.startswith('#'):
                continue
            else:
                ln = line.split(':')
                if len(ln) == 3:
                    ## Call a helper function to create a command
                    cmd = self.createCommand(ln)

                    if (not cmd == ""):
                        commands.append(cmd)
                elif len(ln) == 2:
                    ## This creates a custom command
                    cmd = self.customCommand(ln)

                    if (not cmd == ""):
                        commands.append(cmd)

        ######

        ### Concatenate command from all commands ###

        comm = ""

        for i in commands:
            comm = comm + i + ";"

        comm=comm + "hostname"

        ######

        ### Choose environments and write to script ###

        script_fh.write("#!/bin/bash\n\n")
        script_fh.write("# This script is auto generated\n\n")
        script_fh.write("myuser="+uname+"\n")
        script_fh.write("mypass="+passwd+"\n\n")

        for env in environments:
            if environments[env]:

                script_fh.write("## " + env + " ##\n\n")
                if ',' in vm_groups[env]:
                    script_fh.write("echo -e \"Working on environment "+env+" ...\n\"\n")
                    script_fh.write("for i in {" + vm_groups[env] + "}; do\n\n")
                else:
                    script_fh.write("echo -e \"Working on environment "+env+" ...\n\"\n")
                    script_fh.write("for i in " + vm_groups[env] + "; do\n\n")
                script_fh.write("    /usr/bin/sshpass -p $mypass ssh -o \"StrictHostKeyChecking no\" -o \"UserKnownHostsFile=/dev/null\" $myuser@srv$i " + "\"" +comm+ "\"\n")
                script_fh.write("    echo -e \"\\n-----\\n\"\n\n")
                script_fh.write("done\n\n\n")

        ######

        script_fh.write("########## SCRIPT END ##########\n")

        user_fh.close()
        script_fh.close()

        os.chmod(script_path,0o755)

        return retval


    #### END OF FUNCTION ####

    ##
    # Function that runs the created script
    ##
    def deployScript(self, script_path, wrapper_path, script, username, jumphost):

        retval = Defines.ALL_OK

        fh = open(wrapper_path, "w")

        fh.write("#!/bin/bash\n\n")
        fh.write("#This script is auto generated\n\n")
        fh.write("/usr/bin/scp "+script_path+" "+username+"@"+jumphost+":~/\n")
        fh.write("/usr/bin/ssh "+username+"@"+jumphost+" \"sh ~/"+script+"\"\n\n")
        fh.write("/usr/bin/ssh "+username+"@"+jumphost+" \"rm ~/"+script+"\"\n\n")
        fh.write("########## SCRIPT END ##########\n")

        fh.close()

        os.chmod(wrapper_path,0o755)

        return retval

    #### END OF FUNCTION ####
