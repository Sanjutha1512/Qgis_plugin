# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_addattribute import Ui_AddAttribute
import os, sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class AddAttributeGui(QDialog, QWidget, Ui_AddAttribute):

    inputsignal = pyqtSignal()
    unsetTool = pyqtSignal()
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        
        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)

        self.code_1=None
        self.var1 = None
        self.var2 = None
        self.var3 = None
        self.var4 = None

        self.attribute_list=[]
        self.subclass_items=[]
        self.cancelButton.clicked.connect(self.close_1) 
        self.okButton.clicked.connect(self.append_1)


    @pyqtSlot(str)    
    def assign_value_1(self, text):
        
        if text == "Polygon":
            self.comboBox_3.clear()
            self.comboBox_3.addItems(['','Residential'])
        pass
            

    @pyqtSlot(str)    
    def assign_value_2(self, text):
        if text == "Residential":
            self.code_1='06-0'
            self.lineEdit.setText(self.code_1)
            self.comboBox_2.clear()
            self.subclass_items = ['', 'House', 'Group of houses', 'Apartments']
            self.comboBox_2.addItems(self.subclass_items)
            self.setupUi_1(self)

    @pyqtSlot(str)   
    def assign_value_3(self):

        for n in range(0,4):
            if self.comboBox_2.currentIndex() == n:
                var= str(n)
                self.lineEdit.setText(self.code_1 + var)

    @pyqtSlot(str)
    def add_attribute_1(self, string):
        self.var1 =str(self.comboBox.currentText())
        
    @pyqtSlot(str)
    def add_attribute_2(self, string):
        self.var2 =str(self.comboBox_2.currentText())
    
    @pyqtSlot(str)
    def add_attribute_3(self, string):
        self.var3 =str(self.comboBox_3.currentText())

    @pyqtSlot(str)
    def add_attribute_4(self, string):
        self.var4 =str(self.lineEdit.text())

    def initGui(self):
        
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox.addItems(['','Line', 'Point', 'Polygon'])
        self.lineEdit.clear()

        pass


    def accept(self):
        print "accept"
    
        self.comboBox.activated[str].connect(self.assign_value_1)
        self.comboBox_3.activated[str].connect(self.assign_value_2)
        self.comboBox_2.activated[str].connect(self.assign_value_3)

        self.comboBox_2.currentIndexChanged.connect(self.add_attribute_2)
        self.comboBox.currentIndexChanged.connect(self.add_attribute_1)
        self.comboBox_3.currentIndexChanged.connect(self.add_attribute_3)

        pass

    def append_1(self):
        
        del self.attribute_list[0:4]
        self.attribute_list.append(self.var2)
        self.attribute_list.append(self.var1)
        self.attribute_list.append(self.var3)
        self.attribute_list.append(self.var4)
        self.delUi_1(self)
        print self.attribute_list
        pass


    def close_1(self):
        self.unsetTool.emit()

    
        

