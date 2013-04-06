# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/audit_widget.ui'
#
# Created: Sat Apr  6 14:21:04 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AuditWidget(object):
    def setupUi(self, AuditWidget):
        AuditWidget.setObjectName(_fromUtf8("AuditWidget"))
        AuditWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(AuditWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.toolButton = QtGui.QToolButton(AuditWidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(AuditWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(AuditWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)

        self.retranslateUi(AuditWidget)
        QtCore.QMetaObject.connectSlotsByName(AuditWidget)

    def retranslateUi(self, AuditWidget):
        AuditWidget.setWindowTitle(QtGui.QApplication.translate("AuditWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("AuditWidget", "搜索", None, QtGui.QApplication.UnicodeUTF8))

