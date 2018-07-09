# -*- coding: utf-8 -*-

from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QFileInfo, QSize, QVariant
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QToolBar
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources

# Import the code for the dialog
from quick_digitize_dialog import QuickDigitizeDialog
from vertexfindertool import VertexFinderTool
from rotateobjecttool import RotateObjectTool
from showazimuthtool import ShowAzimuthTool
from addattributetool import AddAttributeTool
from orthogonaldigitizertool import OrthogonalDigitizerTool
from addfieldstool import AddFieldsTool
from addstyletool import AddStyleTool
from createpointlayertool import CreatePointLayerTool
from createlinelayertool import CreateLineLayerTool
from createpolygonlayertool import CreatePolygonLayerTool
from splinetool import SplineTool
from recttool import RectTool
from settingsdialog import SettingsDialog

import os.path, sys
currentPath = os.path.dirname( __file__ )

class QuickDigitize:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgisInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        
        # initialize locale
        # locale = QSettings().value('locale/userLocale')[0:2]
        # locale_path = os.path.join(
        #     self.plugin_dir,
        #     'i18n',
        #     'QuickDigitize_{}.qm'.format(locale))

        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path()+"/python/plugins/QuickDigitize"  
        systemPluginPath = QgsApplication.prefixPath()+"/share/qgis/python/plugins/QuickDigitize"
        locale = QSettings().value("locale/userLocale")
        myLocale = locale[0:2]       
            
        if QFileInfo(userPluginPath).exists():
          pluginPath = userPluginPath+"/i18n/QuickDigitize_"+myLocale+".qm"
        elif QFileInfo(systemPluginPath).exists():
          pluginPath = systemPluginPath+"/i18n/QuickDigitize_"+myLocale+".qm"

        self.locale_path = pluginPath
        if QFileInfo(self.locale_path).exists():
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        # Declare instance attributes
        self.actions = []
        self.dlg=QuickDigitizeDialog()

        self.menu = self.tr(u'&QuickDigitize')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'QuickDigitize')
        self.toolbar.setObjectName(u'QuickDigitize')
        self.createpointlayer= CreatePointLayerTool(self.iface, self.toolbar)
        self.createlinelayer= CreateLineLayerTool(self.iface, self.toolbar)
        self.createpolygonlayer= CreatePolygonLayerTool(self.iface, self.toolbar)
        self.spline= SplineTool(self.iface, self.toolbar)
        self.ortho= OrthogonalDigitizerTool(self.iface,self.toolbar)
        self.rectangle=RectTool(self.iface,self.toolbar)
        self.addattribute = AddAttributeTool(self.iface, self.toolbar)
        self.addfields = AddFieldsTool(self.iface, self.toolbar)
        self.showazimuth = ShowAzimuthTool(self.iface,  self.toolbar)
        self.rotateobject = RotateObjectTool(self.iface,  self.toolbar)
        self.addstyle = AddStyleTool(self.iface, self.toolbar)
        


        toolbars = iface.mainWindow().findChildren(QToolBar)
        for self.toolbar in toolbars:
    		self.toolbar.setIconSize(QSize(48,48))

        self.dlg.lineEdit.clear()
        self.dlg.pushButton.clicked.connect(self.select_output_file)


		

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('QuickDigitize', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        
        # Create the dialog (after translation) and keep reference
        self.dlg = QuickDigitizeDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/QuickDigitize/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Quick Digitize'),
            callback=self.run,
            parent=self.iface.mainWindow())
        self.settingsAction = QAction( QCoreApplication.translate("Spline", "Settings" ), self.iface.mainWindow() )
        self.settingsAction.setObjectName("splineAction")
        self.settingsAction.triggered.connect(self.openSettings)

        self.iface.addPluginToVectorMenu(u"Digitize Spline", self.settingsAction)

        self.settingsAction.triggered.connect(self.openSettings)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&QuickDigitize'),
                action)
            self.iface.removeToolBarIcon(action)
        self.iface.removePluginVectorMenu(u'Digitize Spline',self.settingsAction)

        # remove the toolbar
        del self.toolbar

    def openSettings(self):
        
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.changed.connect( self.spline.settingsChanged)
        self.settingsDialog.show()

    def select_output_file(self):
	    filename = QFileDialog.getSaveFileName(self.dlg, "Select output file ","", '*.*')
	    self.dlg.lineEdit.setText(filename)

    def run(self):
        
        layers = self.iface.legendInterface().layers()
        layer_list = []
        for layer in layers:
     		layer_list.append(layer.name())
     	self.dlg.comboBox.clear()
     	self.dlg.comboBox.addItems(layer_list)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            
            filename = self.dlg.lineEdit.text()
            output_file = open(filename, 'w')

            selectedLayerIndex = self.dlg.comboBox.currentIndex()
            selectedLayer = layers[selectedLayerIndex]
            fields = selectedLayer.pendingFields()
            fieldnames = [field.name() for field in fields]

            for f in selectedLayer.getFeatures():
                line = ','.join(unicode(f[x]) for x in fieldnames) + '\n'
                unicode_line = line.encode('utf-8')
                output_file.write(unicode_line)
            output_file.close()