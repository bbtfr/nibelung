#coding=utf-8

from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QWidget, QDialog, QTreeWidgetItem, QDialogButtonBox, QLabel
from lib.form_generator import *
from views.audit_widget import Ui_AuditWidget
from views.form_dialog import Ui_FormDialog
from models import *

class AuditController(QWidget):
  def __init__(self):
    QWidget.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_AuditWidget()
    self.ui.setupUi(self)

    header = self.ui.treeWidget.header()
    header.resizeSection(0, 50)
    header.resizeSection(2, 300)

    self.ui.treeWidget.doubleClicked.connect(self.showDetail)

    self.detailDialog = QDialog(self)
    self.detailDialog.ui = Ui_FormDialog()
    self.detailDialog.ui.setupUi(self.detailDialog)
    self.detailDialog.ui.buttonBox.setStandardButtons(QDialogButtonBox.Close)

    self.findingFormOptions = [
      {'header': u"检测项信息"},
      {'title': u"用户名"},
      {'title': u"名称"},
      {'title': u"严重级别"},
      {'title': u"详细描述"},
      {'title': u"插件名"},
      {'title': u"插件分组"},
      {'title': u"扫描参数"},
      {'header': u"所属检测相关信息"},
      {'title': u"检测ID"},
      {'title': u"检测用户"},
      {'title': u"检测开始时间"},
      {'title': u"检测完成时间"},
      {'title': u"检测耗时"},
    ]

    generateDetailForm(self.detailDialog.ui.formLayout, self.findingFormOptions)

  def updateScanList(self):
    self.allItemMapper = {}
    self.ui.treeWidget.clear()
    for finding in Finding.all():
      stringList = QStringList([
        unicode(finding.severity),
        unicode(finding.name),
        unicode(finding.message),
        unicode(finding.plugin_name),
        unicode(finding.plugin_group),
        unicode(finding.scan_id), 
      ])
      item = QTreeWidgetItem(self.ui.treeWidget, stringList)
      self.allItemMapper[item] = finding

  def showDetail(self):
    finding = self.allItemMapper[self.ui.treeWidget.currentItem()]
    scan = finding.scan
    formValue = {
      u"名称": unicode(finding.name),
      u"严重级别": unicode(finding.severity),
      u"详细描述": unicode(finding.message),
      u"插件名": unicode(finding.plugin_name),
      u"插件分组": unicode(finding.plugin_group),
      u"扫描参数": unicode(finding.plugin_options),
      u"检测ID": unicode(scan.id),
      u"检测用户": scan.scan_by.username if scan.scan_by else u"未知",
      u"检测开始时间": scan.scan_started_at.strftime('%Y-%m-%d %H:%M'),
      u"检测完成时间": scan.scan_finished_at.strftime('%Y-%m-%d %H:%M'),
      u"检测耗时": str(scan.scan_finished_at - scan.scan_started_at),
    }
    setDetailFormValue(self.findingFormOptions, formValue)
    self.detailDialog.show()

  def show(self):
    self.updateScanList()
    QWidget.show(self)