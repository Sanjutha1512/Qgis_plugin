# -*- coding: latin1 -*-

from PyQt4.QtGui import *
from qgis.core import *
from qgis.PyQt.QtCore import *
from PyQt4 import QtCore
import math
import resources
import sys, csv

## Import own classes and tools.
from addstyle import AddStyleGui
import utils

class AddStyleTool:
    
    def __init__(self, iface,  toolBar):
        self.iface = iface
        self.layer = self.iface.activeLayer()
        self.canvas = self.iface.mapCanvas()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint  
        self.ctrl = AddStyleGui(self.iface.mainWindow(),  flags)
        
        self.act_addstyle = QAction(QIcon(":/plugins/QuickDigitize/icon.png"), QCoreApplication.translate("ctools", "Add Style"),  self.iface.mainWindow())
        
        try:
                if self.layer.isEditable():
                    self.act_addstyle.setEnabled(True)
                    self.layer.editingStopped.connect(self.toggle)
        except:
            pass
            
        else:
            self.act_addstyle.setEnabled(False)
            self.layer.editingStarted.connect(self.toggle)
             
             
        self.act_addstyle.triggered.connect(self.showDialog)
        self.iface.currentLayerChanged["QgsMapLayer *"].connect(self.toggle)
        self.canvas.selectionChanged.connect(self.toggle)
        


        toolBar.addSeparator()
        toolBar.addAction(self.act_addstyle)
        

    def toggle(self):
        if self.layer and self.layer.type() == self.layer.VectorLayer:
            # disconnect all previously connect signals in current layer
            try:
                self.layer.editingStarted.disconnect(self.toggle)
            except:
                pass
            try:
                self.layer.editingStopped.disconnect(self.toggle)
            except:
                pass
            
            # check if current layer is editable and has selected features
            # and decide whether the plugin button should be enable or disable
            if self.layer.isEditable():
                self.act_addstyle.setEnabled(True)
                self.layer.editingStopped.connect(self.toggle)
            # layer is not editable    
            else:
                self.act_addstyle.setEnabled(False)
                self.layer.editingStarted.connect(self.toggle)
        else:
            self.act_addstyle.setEnabled(False)

    def showDialog(self):
        self.ctrl.show()
        self.filepath = self.ctrl.select_style_file()
        self.ctrl.okButton.clicked.connect(self.add_style)
        self.ctrl.okButton.clicked.connect(self.close_func)
        
    def add_style(self):
        self.layer.loadNamedStyle(self.filepath)
        self.layer.triggerRepaint()

    def close_func(self):
        self.ctrl.close()