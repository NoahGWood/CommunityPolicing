#! /usr/bin/python3
from os import path
import sys
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
    if module not in sys.modules:
        return False
    else:
        return True

def main():
    installed = checkInstalled()
    print("Installed:",installed)
    GUI = checkModule('QtCore')
    print("GUI:",GUI)
    if installed is False:
        install()
    elif installed is True:
        if GUI is False:
            CLI()
        elif GUI is True:
            runGUI()

main()
#loggerSetup.main(1,'a','error')
#log('d','error')
#print(__file__)
