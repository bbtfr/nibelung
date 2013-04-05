from scan_controller import ScanController
from audit_controller import AuditController
from access_controller import AccessController
from config.acl import acl, identity

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignal
from views.main_dialog import Ui_MainDialog

class MainController(QDialog):
  def __init__(self):
    QDialog.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_MainDialog()
    self.ui.setupUi(self)

    # mapper of [slot, button]
    self.selectMapper = {
      'access': [self.access, self.ui.accessButton],
      'audit': [self.audit, self.ui.auditButton],
      'scan': [self.scan, self.ui.scanButton],
    }
    self._select = None

    for key, value in self.selectMapper.iteritems():
      value[1].clicked.connect(value[0])
    self.select('scan')

  def access(self):
    self.select('access')

  def audit(self):
    self.select('audit')
  
  def scan(self):
    self.select('scan')

  def select(self, select):
    print select, self._select
    if self._select != select:
      for key, value in self.selectMapper.iteritems():
        if key != select:
          value[1].setChecked(False)
      self._select = select
    self.selectMapper[select][1].setChecked(True)
