from PyQt4.QtGui import QWidget
from views.audit_widget import Ui_AuditWidget
from models import *

class AuditController(QWidget):
  def __init__(self):
    QWidget.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_AuditWidget()
    self.ui.setupUi(self)
