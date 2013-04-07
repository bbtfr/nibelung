# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/access_widget.ui'
#
# Created: Mon Apr  8 00:23:32 2013
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
        self.deleteButton = QtGui.QPushButton(AccessWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.editButton = QtGui.QPushButton(AccessWidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 1, 2, 1, 1)
        self.addButton = QtGui.QPushButton(AccessWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(AccessWidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 4)

        self.retranslateUi(AccessWidget)
        QtCore.QMetaObject.connectSlotsByName(AccessWidget)

    def retranslateUi(self, AccessWidget):
        AccessWidget.setWindowTitle(QtGui.QApplication.translate("AccessWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("AccessWidget", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("AccessWidget", "编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("AccessWidget", "添加", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("AccessWidget", "用户ID", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("AccessWidget", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("AccessWidget", "角色", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("AccessWidget", "创建时间", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("AccessWidget", "更新时间", None, QtGui.QApplication.UnicodeUTF8))

