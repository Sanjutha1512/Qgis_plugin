# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

#Import own classes and tools
from rect import RectByExtentTool

# -*- coding: utf-8 -*-


# initialize Qt resources from file resources.py
import resources

# Main class for the plugin
class RectTool:

    def __init__(self, iface, toolBar):
    # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()


   
        settings = QSettings()
        
        #Set the button on toolbar
        self.rectbyextent = QAction(QIcon(":/plugins/QuickDigitize/rectByExtent.svg"), QCoreApplication.translate("ctools", "Rectangle by extent"),  self.iface.mainWindow())

        self.rectbyextent.setCheckable(True)

        
        #When button clicked connect to said function
        self.rectbyextent.triggered.connect(self.rectbyextenttool)
        self.canvas.mapToolSet.connect(self.deactivate)

        toolBar.addSeparator()
        toolBar.addAction(self.rectbyextent)
        self.rectbyextent.setEnabled(True)
        
        # Get the tool
        self.rectbyextenttool = RectByExtentTool( self.canvas )
    
    #To enable function for creating feature
    def rectbyextenttool(self):          
        self.canvas.setMapTool(self.rectbyextenttool)
        self.rectbyextent.setChecked(True)
        QObject.connect(self.rectbyextenttool, SIGNAL("rbFinished(PyQt_PyObject)"), self.createFeature)  

    #To disable function for creating feature        
    def deactivate(self):
        self.rectbyextent.setChecked(False)
        QObject.disconnect(self.rectbyextenttool, SIGNAL("rbFinished(PyQt_PyObject)"), self.createFeature)
        
       
    def createFeature(self, geom):
        settings = QSettings()
        mc = self.canvas
        layer = mc.currentLayer()
        renderer = mc.mapRenderer()
        layerCRSSrsid = layer.crs().srsid()
        projectCRSSrsid = renderer.destinationCrs().srsid()
        provider = layer.dataProvider()
        f = QgsFeature()
        
        
        #On the Fly reprojection because some tools work only in projectedCRS
        if layerCRSSrsid != projectCRSSrsid:
            geom.transform(QgsCoordinateTransform(projectCRSSrsid, layerCRSSrsid))
                                    
        f.setGeometry(geom)
        
        if not (settings.value("/qgis/digitizing/disable_enter_attribute_values_dialog")):
            self.iface.openFeatureForm( layer, f, False)
        
        layer.beginEditCommand("Feature added")       
        layer.addFeature(f)
        layer.endEditCommand()

        
    def unload(self):
		self.toolBar.removeAction(self.rectbyextent)
		
   
 
