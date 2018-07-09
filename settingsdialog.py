# -*- coding: utf-8 -*-


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from utils import *

from ui_settingsdialog import Ui_SettingsDialog

class SettingsDialog( QDialog, Ui_SettingsDialog ):
    changed = pyqtSignal(name = 'changed')

    def __init__( self, parent = None ):
        super( SettingsDialog, self).__init__(parent )
        self.setupUi( self )
        self.setAttribute( Qt.WA_DeleteOnClose )

        self.tolerance = float( QSettings().value(SETTINGS_NAME + "/tolerance", DEFAULT_TOLERANCE ))
        self.splineToleranceSpinBox.setValue( self.tolerance )

        self.tightness = float( QSettings().value(SETTINGS_NAME + "/tightness", DEFAULT_TIGHTNESS ) )
        self.splineTightnessSpinBox.setValue(  self.tightness )

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        #self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.defaults)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)

    def ok(self):
        self.apply()
        self.close()

    def apply(self):
        QSettings().setValue(SETTINGS_NAME+"/tolerance", self.splineToleranceSpinBox.value())
        QSettings().setValue(SETTINGS_NAME+"/tightness", self.splineTightnessSpinBox.value() )
        self.changed.emit()

    def cancel(self):
        self.close()

    
    def defaults(self):
        self.splineToleranceSpinBox.setValue( DEFAULT_TOLERANCE )
        self.splineTightnessSpinBox.setValue( DEFAULT_TIGHTNESS )
