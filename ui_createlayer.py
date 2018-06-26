# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createlayer.ui'
#
# Created: Mon Jun 25 19:10:04 2018
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

class Ui_CreateLayer(object):
    def setupUi(self, CreateLayer):
        CreateLayer.setObjectName(_fromUtf8("CreateLayer"))
        CreateLayer.resize(513, 230)
        self.buttonBox = QtGui.QDialogButtonBox(CreateLayer)
        self.buttonBox.setGeometry(QtCore.QRect(150, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(CreateLayer)
        self.label.setGeometry(QtCore.QRect(40, 40, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(CreateLayer)
        self.lineEdit.setGeometry(QtCore.QRect(190, 40, 241, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(CreateLayer)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(CreateLayer)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 241, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(CreateLayer)
        self.pushButton.setGeometry(QtCore.QRect(450, 100, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(CreateLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CreateLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateLayer)

    def retranslateUi(self, CreateLayer):
        CreateLayer.setWindowTitle(_translate("CreateLayer", "Create new vector layer", None))
        self.label.setText(_translate("CreateLayer", "Name of layer", None))
        self.label_3.setText(_translate("CreateLayer", "Output file location", None))
        self.pushButton.setText(_translate("CreateLayer", "...", None))

