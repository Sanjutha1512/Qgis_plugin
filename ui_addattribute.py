# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addattribute.ui'
#
# Created: Fri Jun 29 15:43:29 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

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



class Ui_AddAttribute(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(595, 455)
        Dialog.setModal(False)
        self.grid = QtGui.QGridLayout()
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 251, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 140, 251, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 80, 251, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 41, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 200, 111, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupUi_1(self,Dialog):

        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 240, 111, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.show()
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.show()
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 53, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.show()
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 280, 111, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.show()
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_7.show()
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 320, 301, 22))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.show()
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 360, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_8.show()
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 360, 301, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_5.show()
        
        self.retranslateUi_1(Dialog)
        # self.grid = QtGui.QGridLayout()
        # self.grid.addWidget(self.lineEdit_2, 4, 0)
        # self.grid.addWidget(self.lineEdit_3, 5, 0)
        # self.grid.addWidget(self.lineEdit_4, 6, 0)
        # self.grid.addWidget(self.lineEdit_5, 7, 0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
    def delUi_1(self,Dialog):

        self.lineEdit_2.deleteLater()
        self.label_5.deleteLater()
        self.label_6.deleteLater()

        self.lineEdit_3.deleteLater()

        self.label_7.deleteLater()

        self.lineEdit_4.deleteLater()

        self.label_8.deleteLater()

        self.lineEdit_5.deleteLater()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Road Attributes", None))
        self.label.setText(_translate("Dialog", "Geometry", None))
        self.label_2.setText(_translate("Dialog", "Class", None))
        self.label_3.setText(_translate("Dialog", "Subclass", None))
        self.label_4.setText(_translate("Dialog", "Code", None))

    def retranslateUi_1(self, Dialog):
        self.label_5.setText(_translate("Dialog", "Ward Number", None))
        self.label_6.setText(_translate("Dialog", "Road ID", None))
        self.label_7.setText(_translate("Dialog", "Road Name", None))
        self.label_8.setText(_translate("Dialog", "Locality Name", None))
        

