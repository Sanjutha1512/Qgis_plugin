# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.PyQt.QtCore import *

# Initialize Qt resources from file resources.py
#from cadtools import resources

#Import own classes and tools
from spline import Spline

class SplineTool():
    
    def __init__(self, iface,  toolBar):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.layer= self.iface.activeLayer()
        self.mc = self.canvas
        self.tool = None
        
        # Create actions 
        self.action_spline = QAction(QIcon(":/plugins/cadtools/icons/spline.png"), QCoreApplication.translate("ctools", "Create Spline Lines/Polygons"),  self.iface.mainWindow())
        
        self.action_spline.setCheckable(True) 

        try:
            if self.layer.isEditable():
                self.action_spline.setEnabled(True)
                self.layer.editingStopped.connect(self.toggle)
                

        except:
            pass
            
        else:
            self.action_spline.setEnabled(False)
            self.layer.editingStarted.connect(self.toggle)
            
        
        # Connect to signals for button behaviour
        self.count=0
        self.count+=1
        if self.count==1:
            
            self.action_spline.triggered.connect(self.digitize)
            self.count-=1
            

        if self.count==0:
            self.canvas.mapToolSet.connect(self.deactivate)
            self.count+=1
            
        # self.iface.currentLayerChanged.connect(self.toggle)
        
        
        # Add actions to the toolbar
        toolBar.addSeparator()
        toolBar.addAction(self.action_spline)
      
    
        # Get the tool
        self.tool = Spline(self.iface)
        
     
    def digitize(self):
        
        layer = self.mc.currentLayer()
        self.action_spline.setChecked(True)
        if self.action_spline.isChecked():
            self.mc.setMapTool(self.tool)
            print 'call'
            
            self.count-=1
        
               
    
    def deactivate(self):
        if self.count == 0:
            self.action_spline.setChecked(False)
            self.mc.unsetMapTool(self.tool)
            print 'tool'
            
            

        else:
            self.count=1
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
                self.action_spline.setEnabled(True)
                # self.action_spline.setChecked(True)
                self.layer.editingStopped.connect(self.toggle)
           # layer is not editable    
           else:
               
               self.action_spline.setEnabled(False)
               # self.action_spline.setChecked(False)
               self.layer.editingStarted.connect(self.toggle)
               # self.mc.mapToolSet.connect(self.deactivate)
        else:
           self.action_spline.setEnabled(False)
           # self.mc.mapToolSet.connect(self.deactivate)
           # self.action_spline.setChecked(True)    
        
