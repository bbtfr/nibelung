# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/main_dialog.ui'
#
# Created: Sat Apr  6 12:22:18 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(600, 400)
        self.gridLayout = QtGui.QGridLayout(MainDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.accessButton = QtGui.QCommandLinkButton(MainDialog)
        self.accessButton.setCheckable(True)
        self.accessButton.setObjectName(_fromUtf8("accessButton"))
        self.gridLayout.addWidget(self.accessButton, 1, 3, 1, 1)
        self.scrollArea = QtGui.QScrollArea(MainDialog)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 582, 340))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 4)
        self.auditButton = QtGui.QCommandLinkButton(MainDialog)
        self.auditButton.setCheckable(True)
        self.auditButton.setObjectName(_fromUtf8("auditButton"))
        self.gridLayout.addWidget(self.auditButton, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.scanButton = QtGui.QCommandLinkButton(MainDialog)
        self.scanButton.setCheckable(True)
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.gridLayout.addWidget(self.scanButton, 1, 1, 1, 1)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.accessButton.setText(QtGui.QApplication.translate("MainDialog", "用户管理", None, QtGui.QApplication.UnicodeUTF8))
        self.auditButton.setText(QtGui.QApplication.translate("MainDialog", "审计", None, QtGui.QApplication.UnicodeUTF8))
        self.scanButton.setText(QtGui.QApplication.translate("MainDialog", "扫描", None, QtGui.QApplication.UnicodeUTF8))

