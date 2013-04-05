from scan_controller import ScanController
from audit_controller import AuditController
from access_controller import AccessController
from config.acl import acl, identity

class MainController:
  def __init__(self):
    self.select()

  def select(self):
    print '1. Scan'
    print '2. Audit'
    print '3. User Manage'
    select = raw_input()
    if select == '1':
      controller = ScanController()
      controller.scan()
    elif select == '2':
      controller = AuditController()
      controller.show()
    elif select == '3':
      controller = UserManagerController()
      controller.show()
    else:
      self.select()

  def show(self):
    pass
