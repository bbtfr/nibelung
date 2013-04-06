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

    self.ui.listWidget.doubleClicked.connect(self.edit)
    self.updateUserList()

    self.ui.addButton.clicked.connect(self.new)
    self.ui.editButton.clicked.connect(self.edit)
    self.ui.deleteButton.clicked.connect(self.destroy)

    self.formDialog = QDialog(self)
    self.formDialog.ui = Ui_FormDialog()
    self.formDialog.ui.setupUi(self.formDialog)
    self.formDialog.ui.buttonBox.accepted.connect(self.commit)
    self.formDialog.resize(250, 200)

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
    self.formDialog.setWindowTitle(u"创建用户")
    self.formDialog.show()

  def edit(self):
    if not self.currentSelectUser(): return
    formValue = {u"用户名": self.user.username, u"用户角色": self.user.roles}
    setFormValue(self.userFormOptions, formValue)
    self.formDialog.setWindowTitle(u"编辑用户")
    self.formDialog.show()

  def commit(self):
    if self.user:
      self.update()
    else:
      self.user = User()
      self.create()

  def create(self):
    self.parseFormValue()
    # save return True on success, False on failed
    if self.user.save():
      self.updateUserList()
      QDialog.accept(self.formDialog)
    else:
      QMessageBox.information(self, u"创建用户失败", self.user.full_error_messages())
      return

  def update(self):
    self.parseFormValue()
    # save return True on success, False on failed
    if self.user.save():
      self.updateUserList()
      QDialog.accept(self.formDialog)
    else:
      QMessageBox.information(self, u"编辑用户失败", self.user.full_error_messages())
      return

  def destroy(self):
    if not self.currentSelectUser(): return
    if QMessageBox.question(self, u"删除用户", u"您确定要删除用户%s？" % self.user.username,
      QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
      self.user.destroy()
    self.updateUserList()

  def parseFormValue(self):
    formValue = getFormValue(self.userFormOptions)
    # set user fields
    self.user.username = formValue[u"用户名"]
    if formValue[u"密码"] or formValue[u"确认密码"]:
      self.user.password = formValue[u"密码"]
      self.user.password_confirm = formValue[u"确认密码"]
    self.user.roles = self.userRoleMapper[formValue[u"用户角色"]]

  def updateUserList(self):
    self.user = None
    self.allUsers = User.all()
    self.ui.listWidget.clear()
    for user in self.allUsers:
      desciption = "%s (%s)" % (user.username, user._roles)
      self.ui.listWidget.addItem(desciption)

  def currentSelectUser(self):
    index = self.ui.listWidget.currentRow()
    if index < 0:
      QMessageBox.information(self, u"未选中用户", u"请先选中一个用户！")
      return None
    self.user = self.allUsers[index]
    return self.user
