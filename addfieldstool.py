# -*- coding: latin1 -*-
# from PyQt4.QtCore import *
# import sip
# sip.setapi('QString', 1)
from PyQt4.QtGui import *
from qgis.core import *
from qgis.PyQt.QtCore import *
from PyQt4 import QtCore
import math
import resources
import sys, csv

## Import own classes and tools.
from addfieldsgui import AddFieldsGui
import utils

class AddFieldsTool:
    
    def __init__(self, iface,  toolBar):
        self.iface = iface
        self.layer = self.iface.activeLayer()
        self.canvas = self.iface.mapCanvas()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  
        self.ctrl = AddFieldsGui(self.iface.mainWindow(),  flags)
        
        self.act_addfields = QAction(QIcon(":/plugins/QuickDigitize/addfields.png"), QCoreApplication.translate("ctools", "Add Fields"),  self.iface.mainWindow())
        
        try:
                if self.layer.isEditable():
                    self.act_addfields.setEnabled(True)
                    self.layer.editingStopped.connect(self.toggle)
        except:
            pass
            
        else:
            self.act_addfields.setEnabled(False)
            self.layer.editingStarted.connect(self.toggle)
             
             
        self.act_addfields.triggered.connect(self.showDialog)
        self.iface.currentLayerChanged["QgsMapLayer *"].connect(self.toggle)
        self.canvas.selectionChanged.connect(self.toggle)
        


        toolBar.addSeparator()
        toolBar.addAction(self.act_addfields)
        

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
                self.act_addfields.setEnabled(True)
                self.layer.editingStopped.connect(self.toggle)
            # layer is not editable    
            else:
                self.act_addfields.setEnabled(False)
                self.layer.editingStarted.connect(self.toggle)
        else:
            self.act_addfields.setEnabled(False)

    def showDialog(self):
        self.ctrl.initGui()
        self.ctrl.show()
        self.ctrl.select_input_file()

        self.ctrl.okButton.clicked.connect(self.add_field)
        self.ctrl.okButton.clicked.connect(self.close_func)
        pass


    def add_field(self):
        self.fields=[]
        self.field_type=[]
        with open(self.ctrl.inputfile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                a=row[1]
                b=row[2]
                # a=QString(a)
                
                self.fields.append(a)   
                self.field_type.append(b)
                print self.fields
                print self.field_type

        for n in range(1,len(self.fields)):
            if self.fields[n] == "Width":
                self.qgsfields=self.fields[n]
                # self.qgsfields_1=self.field_type[n]
                self.layer.dataProvider().addAttributes([QgsField(self.qgsfields, QVariant.Double)])
            else:
                self.qgsfields=self.fields[n]
                # self.qgsfields_1=self.field_type[n]
                self.layer.dataProvider().addAttributes([QgsField(self.qgsfields, QVariant.String)])
                
        # self.layer.dataProvider().addAttributes([QgsField('asdssa',QVariant.Double)])
        self.layer.updateFields()


    def close_func(self):
        self.ctrl.close()