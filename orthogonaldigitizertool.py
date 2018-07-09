# -*- coding: latin1 -*-
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from orthogonaldigitizer import OrthogonalDigitizer

class OrthogonalDigitizerTool():
    
        def __init__(self, iface,  toolBar):
            # Save reference to the QGIS interface
            self.iface = iface
            self.canvas = self.iface.mapCanvas()
            self.layer= self.iface.activeLayer()
            self.mc = self.canvas
            self.tool = None
            
            self.act_ortho = QAction(QIcon(":/plugins/QuickDigitize/icon.png"), QCoreApplication.translate("ctools", "Capture Orthogonal Lines/Polygons"),  self.iface.mainWindow())
            
            self.act_ortho.setCheckable(True)            
            

            try:
                if self.layer.isEditable():
                    self.act_ortho.setEnabled(True)
                    self.layer.editingStopped.connect(self.toggle)
            except:
                pass
                
            else:
                self.act_ortho.setEnabled(False)
                self.layer.editingStarted.connect(self.toggle)
                
            
            # Connect to signals for button behaviour
            self.count_1=0
            self.count_1+=1
            if self.count_1==1:
                
                self.act_ortho.triggered.connect(self.orthodigitize)
                self.count_1-=1
                

            if self.count_1==0:
                self.canvas.mapToolSet.connect(self.deactivate)
                self.count_1+=1
            # Connect to signals for button behaviour
        
            
            
            # Add actions to the toolbar
            toolBar.addSeparator()
            toolBar.addAction(self.act_ortho)
            
            
            # Get the tool
            self.tool = OrthogonalDigitizer(self.canvas)
                    
        def orthodigitize(self):
            mc = self.canvas
            layer = mc.currentLayer()
            self.act_ortho.setChecked(True)
            # Set OrthogonalTool as current tool
            if self.act_ortho.isChecked():
                self.mc.setMapTool(self.tool)
                print '%d'%self.count_1
                
                self.count_1-=1

        def deactivate(self):
            #uncheck the button/menu 
            if self.count_1 == 0:
                self.act_ortho.setChecked(False)
                self.mc.unsetMapTool(self.tool)
                print '%d hyg' %self.count_1
            else:
                self.count_1=1
                pass

        def toggle(self):
                
            if self.layer:
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
                    self.act_ortho.setEnabled(True)
                    # self.act_ortho.setChecked(True)
                    self.layer.editingStopped.connect(self.toggle)
               # layer is not editable    
               else:
                   
                   self.act_ortho.setEnabled(False)
                   
                   self.layer.editingStarted.connect(self.toggle)
                   
            else:
               self.act_ortho.setEnabled(False)


        
        