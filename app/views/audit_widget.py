# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/audit_widget.ui'
#
# Created: Sun Apr  7 23:33:21 2013
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
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.searchButton = QtGui.QToolButton(AuditWidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 0, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(AuditWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(AuditWidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 4)

        self.retranslateUi(AuditWidget)
        QtCore.QMetaObject.connectSlotsByName(AuditWidget)

    def retranslateUi(self, AuditWidget):
        AuditWidget.setWindowTitle(QtGui.QApplication.translate("AuditWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("AuditWidget", "搜索", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("AuditWidget", "级别", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("AuditWidget", "名称", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("AuditWidget", "详细描述", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("AuditWidget", "插件名", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("AuditWidget", "插件分组", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(5, QtGui.QApplication.translate("AuditWidget", "检测ID", None, QtGui.QApplication.UnicodeUTF8))

