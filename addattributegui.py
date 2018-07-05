# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_addattribute import Ui_AddAttribute
import os, sys, csv
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
    global count
    count =0
    
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
        self.flag = 0
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0

        self.attribute_list=[]
        self.subclass_items=[]
        self.code_1=[]

        self.cancelButton.clicked.connect(self.close_1) 
        self.cancelButton.clicked.connect(self.deletion)
        self.okButton.clicked.connect(self.append_1)
        self.okButton.clicked.connect(self.deletion)

    @pyqtSlot(str)    
    def assign_value_1(self, text):
        
        if text == "Polygon":
            self.comboBox_3.clear()
            self.classes=[]
            with open('C:\Users\Sanjutha Indrajit\.qgis2\python\plugins\QuickDigitize/buildings_class_subclass.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=';')
                for row in readCSV:
                    print(row[0])
                    a=row[0]
                    self.classes.append(a)
                    self.classes[0] = ''
            self.comboBox_3.addItems(self.classes)
            self.c+=1
            # print "assign_value_1 %d" %self.c
        pass
            

    @pyqtSlot(str)    
    def assign_value_2(self, text):

        if self.count>0 and self.flag == 0:
            self.flag=self.delUi_1(self)

        self.subclass=[]
        self.code=[]
        self.subclass_items=[]
        self.code_1=[]
        self.comboBox_2.clear()

        with open('C:\Users\Sanjutha Indrajit\.qgis2\python\plugins\QuickDigitize/buildings_class_subclass.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:

                print(row[2])
                a=row[1]
                b=row[2]
                
                self.subclass.append(a)
                self.code.append(b)
                self.subclass[0] = ''
                self.code[0]= ''

        for n in range(1,len(self.classes)):            
            if text == self.classes[n]:
                # try:
                self.setupUi_1(self)
                # self.a+=1
                # print "assign_value_2 setupUi_1 %d" %n
                # except:
                #     pass
                self.count = n
                #self.count+=1
                count=1
                
                for c in self.subclass[n].split(","):
                    self.subclass_items.append(c)

                self.comboBox_2.addItems(self.subclass_items)

                for g in self.code[n].split(","):
                    self.code_1.append(g)

            else:
                if self.count==1 or self.count==0:

                    pass
                else:
                    self.flag=self.delUi_1(self)
                    self.a-=1
                    print "deletion   %d" %self.a
                    self.comboBox_2.clear()
                    self.d+=1
                    # print "assign_value_2 %d" %self.d
                    
                    self.count-=1


        if n == (len(self.classes)+1) and self.flag ==0 :    
            self.flag=self.delUi_1(self)
            self.count=0
            self.a-=1
            print "deletion   %d" %self.a
            self.comboBox_2.clear()
            self.d+=1
            print "assign_value_2 %d" %self.d

    @pyqtSlot(str)   
    def assign_value_3(self):

        for n in range(0,len(self.subclass_items)):
            if self.comboBox_2.currentIndex() == n:
                self.lineEdit.setText(self.code_1[n])
        self.e+=1
        # print "assign_value_3 %d" %self.e

    @pyqtSlot(str)
    def add_attribute_1(self, string):
        self.var1 =str(self.comboBox.currentText())
        
    @pyqtSlot(str)
    def add_attribute_2(self, string):
        self.var2 =str(self.comboBox_3.currentText())
        if self.var2 == '' and count == 1:
            
            self.delUi_1(self)
            self.a-=1
            print "deletion   %d" %self.a
    
    @pyqtSlot(str)
    def add_attribute_3(self, string):
        self.var3 =str(self.comboBox_2.currentText())

    @pyqtSlot(str)
    def add_attribute_4(self, string):
        self.var4 =str(self.lineEdit.text())

    def initGui(self):
        
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox.addItems(['','Line', 'Point', 'Polygon'])
        self.lineEdit.clear()
        self.count = 0
        self.flag = 0 
        pass


    def accept(self):
        self.b+=1
        # print "accept %d" %self.b
        self.flag =0
        if self.b == 1:
            self.comboBox.activated[str].connect(self.assign_value_1)
            self.comboBox_3.activated[str].connect(self.assign_value_2)
            self.comboBox_2.activated[str].connect(self.assign_value_3)

            self.comboBox_3.currentIndexChanged.connect(self.add_attribute_2)
            self.comboBox.currentIndexChanged.connect(self.add_attribute_1)
            self.comboBox_2.currentIndexChanged.connect(self.add_attribute_3)

    

    def append_1(self):
        
        del self.attribute_list[0:4]
        self.attribute_list.append(self.var2)
        self.attribute_list.append(self.var1)
        self.attribute_list.append(self.var3)
        self.attribute_list.append(self.var4)
          
        print self.attribute_list
        pass


    def close_1(self):
        self.unsetTool.emit()

    @pyqtSlot(str)
    def creation(self):
        self.setupUi_1(self)
        self.a+=1
        # print "Creation %d" %self.a

    @pyqtSlot(str)
    def deletion(self):
        self.delUi_1(self)
        self.a-=1
        print "deletion   %d" %self.a
        

