#! /usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QFileDialog
from PyQt5.QtGui import *
from GUI.wizardGUI import Ui_Wizard
import sys



class my_wizard(QtWidgets.QWizard, Ui_Wizard):
    def __init__(self):
        super(my_wizard, self).__init__()
        self.setupUi(self)
        self.button(QtWidgets.QWizard.NextButton).clicked.connect(self.Next)
        self.button(QtWidgets.QWizard.BackButton).clicked.connect(self.Back)
    def Show_wizard(self):
        mywizard = my_wizard()
        mywizard.exec_()
    def Next(self):
        pid = self.currentId()
        print(pid)

    def Back(self,vid):
        pid = self.currentId()

def Main():
    return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = my_wizard()
    window.show()
    sys.exit(app.exec_())
