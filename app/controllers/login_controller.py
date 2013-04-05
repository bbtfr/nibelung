#coding=utf-8

from models.user import User

from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import pyqtSignal
from views.login_dialog import Ui_LoginDialog

class LoginController(QDialog):

  loggedin = pyqtSignal()

  def __init__(self):
    QDialog.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_LoginDialog()
    self.ui.setupUi(self)

  def accept(self):
    username = unicode(self.ui.usernameLineEdit.text())
    password = unicode(self.ui.passwordLineEdit.text())
    user = User.find_by_username(username)
    if user and user.authenticate(password):
      self.loggedin.emit()
      QDialog.accept(self)
    else:
      QMessageBox.information(self, u"登录失败", u"用户名或密码错误！")