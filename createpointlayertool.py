from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.PyQt.QtCore import *
import resources
import sys,os

## Import own classes and tools.
from createlayergui import CreateLayerGui

class CreatePointLayerTool:
    
    def __init__(self, iface,  toolBar):
        self.iface = iface
        self.layer = self.iface.activeLayer()
        self.canvas = self.iface.mapCanvas()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  
        self.dlg = CreateLayerGui(self.iface.mainWindow(),  flags)
        #self.attribute =[]
        
        self.act_createpointlayer = QAction(QIcon(":/plugins/QuickDigitize/add_point_layer.svg"), QCoreApplication.translate("ctools", "Create Point Layer"),  self.iface.mainWindow())
                     
        self.act_createpointlayer.triggered.connect(self.showDialog)
        

        toolBar.addSeparator()
        toolBar.addAction(self.act_createpointlayer)
        

    def showDialog(self):
   
        self.dlg.initGui()
        self.dlg.show()
        self.dlg.pushButton.clicked.connect(self.select_output_file)
        self.dlg.okButton.clicked.connect(self.close_func)
        pass

    def select_output_file(self):
	    filename = QFileDialog.getSaveFileName(self.dlg, "Select output file ","", '*.shp')
	    self.dlg.lineEdit_2.setText(filename)
	
    def close_func(self):
        self.dlg.close()

	 

