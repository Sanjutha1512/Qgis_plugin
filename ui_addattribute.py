# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addattribute.ui'
#
# Created: Fri Jun 29 15:43:29 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import csv

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



class Ui_AddAttribute(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(632, 736)
        Dialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 690, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 251, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 180, 251, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 41, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 230, 111, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 101, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 20, 251, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 120, 251, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))


        count=0

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupUi_2(self,Dialog):

        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 270, 141, 22))
        # self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.show()
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.show()
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 53, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.show()
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 310, 201, 22))
        # self.lineEdit_3.setMaxLength(15)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.show()
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 350, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_7.show()
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 350, 361, 22))
        # self.lineEdit_4.setMaxLength(30)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.show()
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 390, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_8.show()
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 390, 461, 22))
        # self.lineEdit_5.setMaxLength(50)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_5.show()
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 430, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_9.show()
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 430, 461, 22))
        # self.lineEdit_6.setMaxLength(50)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_6.show()
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 470, 101, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_10.show()
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 470, 41, 22))
        # self.lineEdit_7.setMaxLength(5)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_7.show()
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 520, 101, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_11.show()
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 520, 251, 22))
        # self.lineEdit_8.setMaxLength(15)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_8.show()
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(30, 560, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_12.show()
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 560, 81, 22))
        self.lineEdit_9.setText(_fromUtf8(""))
        # self.lineEdit_9.setMaxLength(10)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_9.show()
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 600, 81, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_13.show()
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 600, 461, 71))
        self.lineEdit_10.setText(_fromUtf8(""))
        # self.lineEdit_10.setMaxLength(50)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_10.show()
        self.retranslateUi_2(Dialog)
        # self.grid = QtGui.QGridLayout()
        # self.grid.addWidget(self.lineEdit_2, 4, 0)
        # self.grid.addWidget(self.lineEdit_3, 5, 0)
        # self.grid.addWidget(self.lineEdit_4, 6, 0)
        # self.grid.addWidget(self.lineEdit_5, 7, 0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupUi_1(self,Dialog):

        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 270, 141, 22))
        # self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.show()
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.show()
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.show()
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 310, 201, 22))
        # self.lineEdit_3.setMaxLength(15)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.show()
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 350, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_7.show()
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 350, 361, 22))
        # self.lineEdit_4.setMaxLength(30)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.show()
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 550, 161, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_8.show()
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 550, 431, 22))
        # self.lineEdit_5.setMaxLength(50)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_5.show()
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 590, 161, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_9.show()
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 600, 431, 22))
        # self.lineEdit_6.setMaxLength(50)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_6.show()
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 640, 211, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_10.show()
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 640, 251, 22))
        # self.lineEdit_7.setMaxLength(5)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_7.show()
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 390, 101, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_11.show()
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 390, 251, 22))
        # self.lineEdit_8.setMaxLength(15)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_8.show()
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(30, 430, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_12.show()
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 430, 81, 22))
        self.lineEdit_9.setText(_fromUtf8(""))
        # self.lineEdit_9.setMaxLength(10)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        # self.lineEdit_9.show()
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(10, 470, 151, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_13.show()
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(190, 470, 81, 21))
        self.lineEdit_10.setText(_fromUtf8(""))
        # self.lineEdit_10.setMaxLength(50)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_10.show()
        self.lineEdit_11 = QtGui.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 500, 421, 31))
        self.lineEdit_11.setText(_fromUtf8(""))
        # self.lineEdit_11.setMaxLength(50)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_11.show()
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(0, 510, 191, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_15.show()
        self.retranslateUi_1(Dialog)
        # self.grid = QtGui.QGridLayout()
        # self.grid.addWidget(self.lineEdit_2, 4, 0)
        # self.grid.addWidget(self.lineEdit_3, 5, 0)
        # self.grid.addWidget(self.lineEdit_4, 6, 0)
        # self.grid.addWidget(self.lineEdit_5, 7, 0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
    def delUi_2(self,Dialog):

            self.lineEdit_2.deleteLater()
            self.label_5.deleteLater()
            self.label_6.deleteLater()
            self.lineEdit_3.deleteLater()
            self.label_7.deleteLater()
            self.lineEdit_4.deleteLater()
            self.label_8.deleteLater()
            self.lineEdit_5.deleteLater()
            self.label_9.deleteLater()
            self.lineEdit_6.deleteLater()
            self.label_10.deleteLater()
            self.lineEdit_7.deleteLater()
            self.label_11.deleteLater()
            self.lineEdit_8.deleteLater()
            self.label_12.deleteLater()
            self.lineEdit_9.deleteLater()
            self.label_13.deleteLater()
            self.lineEdit_10.deleteLater()
            return 1

    def delUi_1(self,Dialog):

            self.lineEdit_2.deleteLater()
            self.label_5.deleteLater()
            self.label_6.deleteLater()
            self.lineEdit_3.deleteLater()
            self.label_7.deleteLater()
            self.lineEdit_4.deleteLater()
            self.label_8.deleteLater()
            self.lineEdit_5.deleteLater()
            self.label_9.deleteLater()
            self.lineEdit_6.deleteLater()
            self.label_10.deleteLater()
            self.lineEdit_7.deleteLater()
            self.label_11.deleteLater()
            self.lineEdit_8.deleteLater()
            self.label_12.deleteLater()
            self.lineEdit_9.deleteLater()
            self.label_13.deleteLater()
            self.lineEdit_10.deleteLater()
            self.lineEdit_11.deleteLater()
            self.label_15.deleteLater()
            return 1


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Attributes", None))
        self.label.setText(_translate("Dialog", "Geometry", None))
        self.label_2.setText(_translate("Dialog", "Class", None))
        self.label_3.setText(_translate("Dialog", "Subclass", None))
        self.label_4.setText(_translate("Dialog", "Code", None))
        self.label_14.setText(_translate("Dialog", "Geo-Spatial Data", None))

    def retranslateUi_2(self, Dialog):
        self.labels=[]
        with open('C:\Users\Sanjutha Indrajit\.qgis2\python\plugins\QuickDigitize/buildings_labels.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                # print(row[0])
                a=row[0]
                self.labels.append(a)
                
        self.label_5.setText(_translate("Dialog", self.labels[4], None))
        self.label_6.setText(_translate("Dialog", self.labels[5], None))
        self.label_7.setText(_translate("Dialog", self.labels[6], None))
        self.label_8.setText(_translate("Dialog", self.labels[7], None))
        self.label_9.setText(_translate("Dialog", self.labels[8], None))
        self.label_10.setText(_translate("Dialog", self.labels[9], None))
        self.label_11.setText(_translate("Dialog", self.labels[10], None))
        self.label_12.setText(_translate("Dialog", self.labels[11], None))
        self.label_13.setText(_translate("Dialog", self.labels[12], None))

    def retranslateUi_1(self, Dialog):
        self.labels=[]
        with open('C:\Users\Sanjutha Indrajit\.qgis2\python\plugins\QuickDigitize/Road_labels.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                # print(row[0])
                a=row[0]
                self.labels.append(a)
                
        self.label_5.setText(_translate("Dialog", self.labels[4], None))
        self.label_6.setText(_translate("Dialog", self.labels[5], None))
        self.label_7.setText(_translate("Dialog", self.labels[6], None))
        self.label_8.setText(_translate("Dialog", self.labels[11], None))
        self.label_9.setText(_translate("Dialog", self.labels[12], None))
        self.label_10.setText(_translate("Dialog", self.labels[13], None))
        self.label_11.setText(_translate("Dialog", self.labels[7], None))
        self.label_12.setText(_translate("Dialog", self.labels[8], None))
        self.label_13.setText(_translate("Dialog", self.labels[9], None))
        self.label_15.setText(_translate("Dialog", self.labels[10], None))
        # self.label_15.setText(_translate("Dialog", self.labels[14], None))
