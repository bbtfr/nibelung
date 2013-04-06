from scan_controller import ScanController
from audit_controller import AuditController
from access_controller import AccessController
from lib.select_mapper import SelectMapper
from config.acl import acl, identity

from PyQt4.QtGui import QDialog
from views.main_dialog import Ui_MainDialog

class MainController(QDialog, SelectMapper):
  def __init__(self):
    QDialog.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_MainDialog()
    self.ui.setupUi(self)

    self.ui.accessWidget = AccessController()
    self.ui.auditWidget = AuditController()
    self.ui.scanWidget = ScanController()

    # mapper of [slot, button]
    self.selectMapper = {
      'access': {
        'button': self.ui.accessButton,
        'widget': self.ui.accessWidget,
      },
      'audit': {
        'button': self.ui.auditButton,
        'widget': self.ui.auditWidget,
      },
      'scan': {
        'button': self.ui.scanButton,
        'widget': self.ui.scanWidget,
      },
    }

    for key, value in self.selectMapper.iteritems():
      value['widget'].hide()
      self.ui.horizontalLayout.addWidget(value['widget'])
      
    # setup select mapper which defined in app/lib/select_mapper.py
    self.setupSelectMapper(self.selectMapper)
    
    self.select('scan')
