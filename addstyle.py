from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_addstyle import Ui_AddStyle
import os, sys

class AddStyleGui(QDialog, QWidget, Ui_AddStyle):

    unsetTool = pyqtSignal()
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        
        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.cancelButton.clicked.connect(self.close_1) 
        
    def select_style_file(self):
        filename = QFileDialog.getOpenFileName(self, "Select style file ","", '*.qml')
        self.lineEdit.setText(filename)
        self.stylefile= self.lineEdit.text()
        return self.stylefile
        
    def close_1(self):
        self.unsetTool.emit()