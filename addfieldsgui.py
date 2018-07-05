from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_addfield import Ui_AddField
import os, sys

class AddFieldsGui(QDialog, QWidget, Ui_AddField):

    inputsignal = pyqtSignal()
    unsetTool = pyqtSignal()
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        
        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)


        self.cancelButton.clicked.connect(self.close_1) 
        #self.okButton.clicked.connect(self.Point)
        self.lineEdit.clear()

    def initGui(self):
        self.lineEdit.clear()
        pass

    def select_input_file(self):
        filename = QFileDialog.getOpenFileName(self, "Select input file ","", '*.csv')
        self.lineEdit.setText(filename)
        self.inputfile= self.lineEdit.text()

    
    def close_1(self):
        self.unsetTool.emit()