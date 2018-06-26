# -*- coding: latin1 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.PyQt.QtCore import *
import math
import resources
import sys

## Import own classes and tools.
from addattributegui import AddAttributeGui
from vertexandobjectfindertool import VertexAndObjectFinderTool
import utils

class AddAttributeTool:
    
    def __init__(self, iface,  toolBar):
        self.iface = iface
        self.layer = self.iface.activeLayer()
        self.canvas = self.iface.mapCanvas()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  
        self.ctrl = AddAttributeGui(self.iface.mainWindow(),  flags)
        #self.attribute =[]
        self.attribute = self.ctrl.attribute_list

        
        self.p1 = None
        self.m1 = None
        self.feat = None
        self.rb = None
        
        self.act_addattribute = QAction(QIcon(":/plugins/QuickDigitize/icon.png"), QCoreApplication.translate("ctools", "Add Attributes"),  self.iface.mainWindow())
        self.act_selectvertexandobject= QAction(QIcon(":/plugins/cadtools/icons/selectvertexandfeature.png"), QCoreApplication.translate("ctools", "Select Vertex and Object"),  self.iface.mainWindow())
        self.act_selectvertexandobject.setCheckable(True)
             
        self.act_addattribute.triggered.connect(self.showDialog)
        self.canvas.mapToolSet.connect(self.deactivate)

        toolBar.addSeparator()
        toolBar.addAction(self.act_selectvertexandobject)
        toolBar.addAction(self.act_addattribute)

        
        self.act_selectvertexandobject.triggered.connect(self.selectvertexandobject)
        self.canvas.mapToolSet.connect(self.deactivate)
  
            
        self.tool = VertexAndObjectFinderTool(self.canvas)   


    def selectvertexandobject(self):
        mc = self.canvas
        mc.setMapTool(self.tool)
        
        self.act_selectvertexandobject.setChecked(True)       
 
        self.tool.vertexAndObjectFound.connect(self.storeVertexAndObject)
 
        pass
        
    
    def storeVertexAndObject(self,  result):
        self.p1 = result[0]
        self.feat = result[1]
        self.m1 = result[2]
        self.rb = result[3]

    def showDialog(self):

        if self.p1 == None or self.feat == None:
            QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), QCoreApplication.translate("ctools", "Not enough objects selected."))
        else:
           
            self.ctrl.initGui()
            self.ctrl.show()
            self.ctrl.accept()
            
            self.ctrl.okButton.clicked.connect(self.newattribute)
            self.ctrl.okButton.clicked.connect(self.close_func)
        pass


    def newattribute(self):
        self.attribute = self.ctrl.attribute_list
        self.newfeature = QgsFeature(self.layer.fields())
        self.newfeature_list = self.layer.selectedFeatures()
        self.newfeature = self.newfeature_list[0]
        self.layer.startEditing()
        self.layer.updateFields()
        
        self.newfeature.setAttributes(self.attribute)
        self.layer.updateFeature(self.newfeature)
        self.layer.commitChanges()
        del self.newfeature
        del self.attribute

    def deactivate(self):
        self.p1 = None
        self.act_selectvertexandobject.setChecked(False)

    def close_func(self):
        self.ctrl.close()

    
    
