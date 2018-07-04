# -*- coding: utf-8 -*-
#-----------------------------------------------------------
# 
# Rectangles Ovals Digitizing
# Copyright (C) 2011 - 2012 Pavol Kapusta
# pavol.kapusta@gmail.com
# bug fix in version 1.1.3 added by Thomas Baumann rdbath.regiodata@gmail.com
# Code adopted/adapted from:
#
# 'SelectPlus Menu Plugin', Copyright (C) Barry Rowlingson
# 'CadTools Plugin', Copyright (C) Stefan Ziegler
# 'Numerical Vertex Edit Plugin' and 'traceDigitize' plugin, Copyright (C) Cédric Möri
#
#-----------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------


# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

#Import own classes and tools
from rectovaldigittools import RectByExtentTool

# initialize Qt resources from file resources.py
import resources

# Our main class for the plugin
class RectOvalDigit:

    def __init__(self, iface, toolBar):
    # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()


   
        settings = QSettings()
        # Add button
        # Add actions
        # self.rectbyextent = QAction(QIcon(":/plugins/rectovalDigit/icons/rectbyextent.png"),  "Rectangle by extent",  self.iface.mainWindow())
        self.rectbyextent = QAction(QIcon(":/plugins/rectovalDigit/icons/rectbyextent.png"), QCoreApplication.translate("ctools", "Rectangle by extent"),  self.iface.mainWindow())

        self.rectbyextent.setCheckable(True)
        # self.rectbyextent.setEnabled(False)
        
        
    
        self.rectbyextent.triggered.connect(self.rectbyextentdigit )
        self.canvas.mapToolSet.connect(self.deactivate)

        toolBar.addSeparator()
        toolBar.addAction(self.rectbyextent)
        self.rectbyextent.setEnabled(True)
        
        # Get the tools
        self.rectbyextenttool = RectByExtentTool( self.canvas )
    
    def rectbyextentdigit(self):          
        self.canvas.setMapTool(self.rectbyextenttool)
        self.rectbyextent.setChecked(True)
        QObject.connect(self.rectbyextenttool, SIGNAL("rbFinished(PyQt_PyObject)"), self.createFeature)  

            
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
        
        
        #On the Fly reprojection.
        if layerCRSSrsid != projectCRSSrsid:
            geom.transform(QgsCoordinateTransform(projectCRSSrsid, layerCRSSrsid))
                                    
        f.setGeometry(geom)
        
        # add attribute fields to feature
        fields = layer.pendingFields()

        # vector api change update

        f.initAttributes(fields.count())
        for i in range(fields.count()):
            f.setAttribute(i,provider.defaultValue(i))

        if not (settings.value("/qgis/digitizing/disable_enter_attribute_values_dialog")):
            self.iface.openFeatureForm( layer, f, False)
        
        layer.beginEditCommand("Feature added")       
        layer.addFeature(f)
        layer.endEditCommand()


    def changegeom(self, result):
        mc = self.canvas
        layer = mc.currentLayer()
        renderer = mc.mapRenderer()
        layerCRSSrsid = layer.crs().srsid()
        projectCRSSrsid = renderer.destinationCrs().srsid()
        geom = result[0]
        fid = result[1]
        if layerCRSSrsid != projectCRSSrsid:
            geom.transform(QgsCoordinateTransform(projectCRSSrsid, layerCRSSrsid))
        layer.beginEditCommand("Feature rotated")
        layer.changeGeometry( fid, geom )
        layer.endEditCommand()
        
    def unload(self):
		self.toolBar.removeAction(self.rectbyextent)
		
   
 
