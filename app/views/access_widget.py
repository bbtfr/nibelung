# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/access_widget.ui'
#
# Created: Sat Apr  6 14:26:57 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccessWidget(object):
    def setupUi(self, AccessWidget):
        AccessWidget.setObjectName(_fromUtf8("AccessWidget"))
        AccessWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(AccessWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.addButton = QtGui.QPushButton(AccessWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)
        self.editButton = QtGui.QPushButton(AccessWidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 1, 2, 1, 1)
        self.deleteButton = QtGui.QPushButton(AccessWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 1, 3, 1, 1)
        self.listWidget = QtGui.QListWidget(AccessWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 4)

        self.retranslateUi(AccessWidget)
        QtCore.QMetaObject.connectSlotsByName(AccessWidget)

    def retranslateUi(self, AccessWidget):
        AccessWidget.setWindowTitle(QtGui.QApplication.translate("AccessWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("AccessWidget", "添加", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("AccessWidget", "编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("AccessWidget", "删除", None, QtGui.QApplication.UnicodeUTF8))

