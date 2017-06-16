#! /usr/bin/python3
from os import path, system
from sys import modules
import loggerSetup


def log(level,e):
    script = __file__
    loggerSetup.main(script,level,str(e))

def check_installed():
    if path.isfile('installed'):
        return True
    else:
        return False
    
def get_os():
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        print(platform)
        #run linux installation
        return
    elif platform == "darwin":
        #run OSX installation
        return
    elif platform == "win32":
        #run windblows installation
        return
    
        
def install():
    #do magic
    print('installing')
    return

def checkModule(module):
    if module not in modules:
        return False
    else:
        return True

def CLI():
    #if linux do:
#    system("gnome-terminal -e 'bash -c \"dbdriver; exec bash\"'")
    #if windows do:
#    from sys import executable
#    from subprocess import popen, CREATE_NEW_CONSOLE
#    popen([executable, 'dbDriver.py'], creationflags=CREATE_NEW_CONSOLE)
#    input('Enter to exit from this launcher script')
    
def main():
    
    installed = check_installed()
    print("Installed:",installed)
    GUI = checkModule('QtCore')
    print("GUI:",GUI)
    if installed is False:
        if GUI is False:
            CLI()
#        install()
        raise SystemExit
    elif installed is True:
        if GUI is False:
            CLI()
        elif GUI is True:
            runGUI()

main()
