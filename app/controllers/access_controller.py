#coding=utf-8

from PyQt4.QtGui import QWidget, QDialog, QMessageBox
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
from lib.form_generator import *
from views.access_widget import Ui_AccessWidget
from views.form_dialog import Ui_FormDialog
from models import *

class AccessController(QWidget):
  def __init__(self):
    QWidget.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_AccessWidget()
    self.ui.setupUi(self)

    self.updateUserList()

    self.ui.addButton.clicked.connect(self.new)
    self.ui.editButton.clicked.connect(self.edit)
    self.ui.deleteButton.clicked.connect(self.destroy)

    self.formDialog = QDialog(self)
    self.formDialog.ui = Ui_FormDialog()
    self.formDialog.ui.setupUi(self.formDialog)
    self.formDialog.ui.buttonBox.accepted.connect(self.commit)

    self.userRoleMapper = {
      u"用户": "staff",
      u"审计员": "audit",
      u"管理员": "admin",
    }

    self.userFormOptions = [
      {'title': u"用户名", 'type': String},
      {'title': u"密码", 'type': String},
      {'title': u"确认密码", 'type': String},
      {'title': u"用户角色", 'type': List, 'list': self.userRoleMapper.keys()},
    ]

    generateForm(self.formDialog.ui.formLayout, self.userFormOptions)

  def new(self):
    setFormValue(self.userFormOptions, {})
    self.user = None
    self.formDialog.show()

  def edit(self):
    if not self.currentSelectUser(): return
    formValue = {u"用户名": self.user.username, u"用户角色": self.user.roles}
    setFormValue(self.userFormOptions, formValue)
    self.formDialog.show()

  def commit(self):
    if self.user:
      user = self.user
      errorTitle = u"修改用户失败"
    else:
      user = User()
      errorTitle = u"创建用户失败"
    formValue = getFormValue(self.userFormOptions)

    # set user fields
    user.username = formValue[u"用户名"]
    if formValue[u"密码"] or formValue[u"确认密码"]:
      user.password = formValue[u"密码"]
      user.password_confirm = formValue[u"确认密码"]
    user.roles = self.userRoleMapper[formValue[u"用户角色"]]

    # save return True on success, False on failed
    if user.save():
      self.updateUserList()
      QDialog.accept(self.formDialog)
    else:
      errorMessage = "\n".join(user.errors.values())
      QMessageBox.information(self, errorTitle, errorMessage)
      return

  def updateUserList(self):
    self.user = None
    self.allUsers = User.all()
    self.ui.listWidget.clear()
    for user in self.allUsers:
      desciption = "%s (%s)" % (user.username, user._roles)
      self.ui.listWidget.addItem(desciption)

  def destroy(self):
    if not self.currentSelectUser(): return
    if QMessageBox.question(self, u"删除用户", u"您确定要删除用户%s？" % self.user.username,
      QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
      self.user.destroy()
    self.updateUserList()

  def currentSelectUser(self):
    index = self.ui.listWidget.currentRow()
    if index < 0:
      QMessageBox.information(self, u"未选中用户", u"请先选中一个用户！")
      return None
    self.user = self.allUsers[index]
    return self.user