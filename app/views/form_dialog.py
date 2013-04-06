# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/form_dialog.ui'
#
# Created: Sat Apr  6 20:17:00 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormDialog(object):
    def setupUi(self, FormDialog):
        FormDialog.setObjectName(_fromUtf8("FormDialog"))
        FormDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(FormDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(FormDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)

        self.retranslateUi(FormDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FormDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FormDialog)

    def retranslateUi(self, FormDialog):
        FormDialog.setWindowTitle(QtGui.QApplication.translate("FormDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

