# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/scan_widget.ui'
#
# Created: Sun Apr  7 23:11:27 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScanWidget(object):
    def setupUi(self, ScanWidget):
        ScanWidget.setObjectName(_fromUtf8("ScanWidget"))
        ScanWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(ScanWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(ScanWidget)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 249))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.widgetVerticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.widgetVerticalLayout.setObjectName(_fromUtf8("widgetVerticalLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 2, 2)
        spacerItem = QtGui.QSpacerItem(232, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(ScanWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.buttonVerticalLayout = QtGui.QVBoxLayout()
        self.buttonVerticalLayout.setObjectName(_fromUtf8("buttonVerticalLayout"))
        self.allButton = QtGui.QPushButton(ScanWidget)
        self.allButton.setCheckable(True)
        self.allButton.setChecked(False)
        self.allButton.setObjectName(_fromUtf8("allButton"))
        self.buttonVerticalLayout.addWidget(self.allButton)
        self.gridLayout.addLayout(self.buttonVerticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ScanWidget)
        QtCore.QMetaObject.connectSlotsByName(ScanWidget)

    def retranslateUi(self, ScanWidget):
        ScanWidget.setWindowTitle(QtGui.QApplication.translate("ScanWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ScanWidget", "开始检测", None, QtGui.QApplication.UnicodeUTF8))
        self.allButton.setText(QtGui.QApplication.translate("ScanWidget", "所有设置", None, QtGui.QApplication.UnicodeUTF8))

