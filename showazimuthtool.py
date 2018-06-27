# -*- coding: latin1 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from QuickDigitize import resources

## Import own classes and tools.
from vertexfindertool import VertexFinderTool
from showazimuthgui import ShowAzimuthGui
from azimuth import Azimuth
#import cadutils

class ShowAzimuthTool:
    
        def __init__(self, iface,  toolBar):
            # Save reference to the QGIS interface
            self.iface = iface
            self.canvas = self.iface.mapCanvas()
            self.layer=self.iface.activeLayer()
            
            # Points and Markers
            self.p1 = None
            self.p2 = None
            self.m1 = None
            self.m2 = None            
            
            # Create actions 
            self.act_show_azimuth = QAction(QIcon(':plugins/cadtools/icons/showazimuth.png'), QCoreApplication.translate("QuickDigitize", "Show Azimuth"),  self.iface.mainWindow())
            self.act_s2v= QAction(QIcon(':plugins/cadtools/icons/select2vertex.png'), QCoreApplication.translate("QuickDigitize", "Select 2 Vertex Points"),  self.iface.mainWindow())
            self.act_s2v.setCheckable(True)     
            if self.layer.isEditable():
                self.act_show_azimuth.setEnabled(True)
                self.act_s2v.setEnabled(True)
                self.layer.editingStopped.connect(self.toggle)
            else:
                self.act_show_azimuth.setEnabled(False)
                self.act_s2v.setEnabled(False)
                self.layer.editingStarted.connect(self.toggle)
                 
            
            self.iface.currentLayerChanged["QgsMapLayer *"].connect(self.toggle)
            self.canvas.selectionChanged.connect(self.toggle)
                 
            # Connect to signals for button behaviour      
            self.act_show_azimuth.triggered.connect(self.showDialog)
            self.act_s2v.triggered.connect(self.s2v)
            self.canvas.mapToolSet.connect(self.deactivate)

            toolBar.addSeparator()
            toolBar.addAction(self.act_s2v)
            toolBar.addAction(self.act_show_azimuth)
                        
            # Get the tool
            self.tool = VertexFinderTool(self.canvas) 


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
                    self.act_show_azimuth.setEnabled(True)
                    self.act_s2v.setEnabled(True)
                    self.layer.editingStopped.connect(self.toggle)
                # layer is not editable    
                else:
                    self.act_show_azimuth.setEnabled(False)
                    self.act_s2v.setEnabled(False)
                    self.layer.editingStarted.connect(self.toggle)
            else:
                self.act_show_azimuth.setEnabled(False)
                self.act_s2v.setEnabled(False)       
            
        def s2v(self):
            mc = self.canvas
            layer = mc.currentLayer()

            # Set VertexFinderTool as current tool
            mc.setMapTool(self.tool)
            self.act_s2v.setChecked(True)                    
            
            #Connect to the VertexFinderTool
            self.tool.vertexFound.connect(self.storeVertexPointsAndMarkers)

        def storeVertexPointsAndMarkers(self,  result):
            self.p1 = result[0]
            self.p2 = result[1]
            self.m1 = result[2]
            self.m2 = result[3]
            
    
        def showDialog(self):
            if self.p1 == None or self.p2 == None:
                QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), QCoreApplication.translate("ctools", "Not enough vertex selected."))
            else:
                az = Azimuth.calculate(self.p1,  self.p2)
                
                flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  # QgisGui.ModalDialogFlags
                self.ctrl = ShowAzimuthGui(self.iface.mainWindow(),  flags)
                self.ctrl.initGui()
                self.ctrl.show()
                self.ctrl.writeAzimuth(az)
                
                # connect the signals
#                self.ctrl.distancesFromPoints.connect(self.calculateArcIntersection)
#                self.ctrl.closeArcIntersectionGui.connect(self.deactivate)
                self.ctrl.unsetTool.connect(self.unsetTool)
            
            
        def unsetTool(self):
            self.m1 = None
            self.m2 = None
            mc = self.canvas
            mc.unsetMapTool(self.tool)             
            
            
        def deactivate(self):
            self.p1 = None
            self.p2 = None
            #uncheck the button/menu and get rid off the SFtool signal
            self.act_s2v.setChecked(False)
            

