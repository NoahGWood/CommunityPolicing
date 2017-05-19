#! /usr/bin/python3
from os import path
from sys import modules
import loggerSetup
def log(level,e):
    script = __file__
    loggerSetup.main(script,level,str(e))

def checkInstalled():
    if path.isfile('installed'):
        return True
    else:
        return False

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
    #run Command Line Tools
    #ncurses?
    print("Command line tools")

def main():
    installed = checkInstalled()
    print("Installed:",installed)
    GUI = checkModule('QtCore')
    print("GUI:",GUI)
    if installed is False:
        install()
        raise SystemExit
    elif installed is True:
        if GUI is False:
            CLI()
        elif GUI is True:
            runGUI()

main()
