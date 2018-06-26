from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_createlayer import Ui_CreateLayer
import os, sys

class CreateLineLayerGui(QDialog, QWidget, Ui_CreateLayer):

    inputsignal = pyqtSignal()
    unsetTool = pyqtSignal()
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        
        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)


        self.cancelButton.clicked.connect(self.close_1) 
        self.okButton.clicked.connect(self.Point)
        self.lineEdit.clear()

    def initGui(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

        pass

    def Point(self):
        name_of_layer= self.lineEdit.text()
        vl = QgsVectorLayer("LineString", name_of_layer, "memory")
        pr = vl.dataProvider()
        vl.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayer(vl, True)


    
    def close_1(self):
        self.unsetTool.emit()