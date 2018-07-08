# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import math

# Tool class
class RectByExtentTool(QgsMapTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self,canvas)
        self.canvas=canvas

        #Rubberband for outline of feature
        self.rb=None

        #First canvas click coordinates
        self.x0 = None
        self.y0 = None

        #Customized cursor
        self.cursor = QCursor(QPixmap(["16 16 3 1",
                                       "      c None",
                                       ".     c #FF0000",
                                       "+     c #17a51a",
                                       "                ",
                                       "       +.+      ",
                                       "      ++.++     ",
                                       "     +.....+    ",
                                       "    +.  .  .+   ",
                                       "   +.   .   .+  ",
                                       "  +.    .    .+ ",
                                       " ++.    .    .++",
                                       " ... ...+... ...",
                                       " ++.    .    .++",
                                       "  +.    .    .+ ",
                                       "   +.   .   .+  ",
                                       "   ++.  .  .+   ",
                                       "    ++.....+    ",
                                       "      ++.++     ",
                                       "       +.+      "]))
                                  
 
    def canvasPressEvent(self,event):
		layer = self.canvas.currentLayer()
		color = QColor(255,0,0)
		self.rb = QgsRubberBand(self.canvas, True)
		self.rb.setColor(color)
		self.rb.setWidth(1)

    #First screen click coordinates
		x = event.pos().x()
		y = event.pos().y()

    #transformation from screen coordinates to layer's coordinates
		point = self.toLayerCoordinates(layer,event.pos())	

    #transformation from layer coordinates to map's coordinates	
		pointMap = self.toMapCoordinates(layer, point)

    #First map coordinates
		self.x0 = pointMap.x()
		self.y0 = pointMap.y()		
		if self.rb:return
		    
    def canvasMoveEvent(self,event):
        if not self.rb:return
        #track second coordinate (from screen to map)
        currpoint = self.toMapCoordinates(event.pos())

        #Second map coordinates
        currx = currpoint.x()
        curry = currpoint.y()

        self.rb.reset(True)

        #Entire set of coordinates for rectangle
        pt1 = (self.x0, self.y0)
        pt2 = (self.x0, curry)
        pt3 = (currx, curry)
        pt4 = (currx, self.y0)

        points = [pt1, pt2, pt3, pt4]
        polygon = [QgsPoint(i[0],i[1]) for i in points]

        #Create Rectangle with x axis as horizontal
	self.rb.setToGeometry(QgsGeometry.fromPolygon([polygon]), None)
        #delete [self.rb.addPoint( point ) for point in polygon]                
        
    def canvasReleaseEvent(self,event):
        if not self.rb:return		

        #Check if enough coordinates for rectangle
        if self.rb.numberOfVertices() > 2:
            geom = self.rb.asGeometry()
            self.emit(SIGNAL("rbFinished(PyQt_PyObject)"), geom)
            
        self.rb.reset(True)
        self.rb=None
        self.canvas.refresh()

    def showSettingsWarning(self):
        pass
    
    def activate(self):
        self.canvas.setCursor(self.cursor)
        
    def deactivate(self):
        pass

    def isZoomTool(self):
        return False
  
    def isTransient(self):
        return False
    
    def isEditTool(self):
        return True

