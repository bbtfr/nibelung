from PyQt4.QtGui import QWidget
from views.audit_widget import Ui_AuditWidget
from models import *

class AuditController(QWidget):
  def __init__(self):
    QWidget.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_AuditWidget()
    self.ui.setupUi(self)

    self.ui.listWidget.doubleClicked.connect(self.updateFindingList)

  def updateScanList(self):
    self.allScan = Scan.all()
    self.ui.listWidget.clear()
    for scan in self.allScan:
      desciption = "Scan %d (%s) include %d findings" % (scan.id, scan.scan_by, scan.findings_num)
      self.ui.listWidget.addItem(desciption)

  def updateFindingList(self, index):
    self.scan = self.allScan[index.row()]
    self.ui.listWidget.clear()
    for finding in self.scan.findings:
      desciption = "%s (%s)" % (finding.id, finding.message)
      self.ui.listWidget.addItem(desciption)

  def show(self):
    self.updateScanList()
    QWidget.show(self)