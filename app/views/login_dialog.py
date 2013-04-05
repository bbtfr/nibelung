# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/loginDialog.ui'
#
# Created: Fri Apr  5 20:30:11 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(300, 150)
        self.gridLayout = QtGui.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.usernameLineEdit = QtGui.QLineEdit(LoginDialog)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(LoginDialog)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(LoginDialog)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout.addWidget(self.passwordLineEdit, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(LoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.usernameLabel = QtGui.QLabel(LoginDialog)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "登陆", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("LoginDialog", "密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("LoginDialog", "用户名：", None, QtGui.QApplication.UnicodeUTF8))

