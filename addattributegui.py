# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_addattribute import Ui_AddAttribute
import os, sys

class AddAttributeGui(QDialog, QWidget, Ui_AddAttribute):

    inputsignal = pyqtSignal()
    unsetTool = pyqtSignal()
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        
        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)


        self.var1 = None
        self.var2 = None
        self.attribute_list=[]
        self.cancelButton.clicked.connect(self.close_1) 
        self.okButton.clicked.connect(self.append_1)


    @pyqtSlot(str)    
    def assign_value_1(self, text):
        if text == "Line":
            self.comboBox_2.clear()
            self.comboBox_2.addItems([' ','2','3'])
            
        if text == "Polygon":
            self.comboBox_2.clear()
            self.comboBox_2.addItems([' ','1','4'])
        pass
            

    @pyqtSlot(str)    
    def assign_value_2(self, text):
        if text == "1":
            self.lineEdit.setText('Hi')
        if text == "2":
            self.lineEdit.setText('Hi1')
        if text == "3":
            self.lineEdit.setText('Bye')
        if text == "4":
            self.lineEdit.setText('Bye1')

    @pyqtSlot(str)
    def add_attribute_1(self, string):
        self.var1=str(self.comboBox.currentText())
        
    @pyqtSlot(str)
    def add_attribute_2(self, string):
        self.var2=str(self.comboBox_2.currentText())
        

    # @pyqtSlot(str)   
    # def assign_value_3(self):
    #     var3 = self.lineEdit.value()
    #     return var3

    def initGui(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(['','Line', 'Polygon'])
        # self.comboBox_2.addItems(['1','2','3','4'])
        #line=raw_input()
        self.lineEdit.setText('')

        pass

        
    # def acceptattribute(self):
    #     attribute_list = []
    #     #self.inputsignal.emit()
    #     self.comboBox.activated[str].connect(self.assign_value_1)
    #     var1=str(self.comboBox.currentText())
    #     attribute_list.append(var1)
    #     # if 'Line'== var1:
    #     #     self.comboBox_2.clear()
    #     #     self.comboBox_2.addItems([' ','2','3'])
    #     #     self.inputsignal.emit()
    #     self.comboBox_2.activated[str].connect(self.assign_value_2)
    #     var2=str(self.comboBox_2.currentText())
    #     attribute_list.append(var2)
    #     #     if '1' == var2:
    #     #         self.lineEdit.setText('Hi')
    #     #     else:
    #     #         self.lineEdit.setText('Hi1')
    #     # else:
    #     #     self.comboBox_2.clear()
    #     #     self.comboBox_2.addItems([' ','1','4'])
    #     #     #self.inputsignal.emit()
    #     #     var2 = self.comboBox_2.activated[str].connect(self.assign_value_2)
    #     #     var2=str(var2)
    #     #     if '2' == var2:
    #     #         self.lineEdit.setText('Bye')
    #     #     else :
    #     #         self.lineEdit.setText('Bye2')
    #     #self.inputsignal.emit()
    #     #var3 = self.lineEdit.connect(self.assign_value_3)
    #     #attribute_list.append(var3)

    #     print attribute_list


    def accept(self):
        print "accept"
    
        self.comboBox.activated[str].connect(self.assign_value_1)
        self.comboBox_2.activated[str].connect(self.assign_value_2)

        self.comboBox_2.currentIndexChanged.connect(self.add_attribute_2)
        self.comboBox.currentIndexChanged.connect(self.add_attribute_1)
        
    
        pass

    def append_1(self):
        
        del self.attribute_list[0:2]
        self.attribute_list.append(self.var2)
        self.attribute_list.append(self.var1)
        
        print self.attribute_list
        pass


    def close_1(self):
        self.unsetTool.emit()


