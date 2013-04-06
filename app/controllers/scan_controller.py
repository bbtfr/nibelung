#coding=utf-8

from datetime import datetime
from lib.plugin_manager import DirectoryPluginManager
from lib.select_mapper import SelectMapper
from lib.form_generator import generateForm, getFormValue
from config import session
from models import *

from PyQt4.QtGui import QWidget, QPushButton, QFormLayout, QMessageBox, QRegExpValidator
from PyQt4.QtCore import pyqtSignal, QSignalMapper, SIGNAL
from PyQt4.QtCore import QObject, QString, QRegExp
from views.scan_widget import Ui_ScanWidget

class ScanController(QWidget, SelectMapper):
  def __init__(self):
    QWidget.__init__(self)

    # Set up the user interface from Designer.
    self.ui = Ui_ScanWidget()
    self.ui.setupUi(self)

    # init plugin manager
    self.pluginManager = DirectoryPluginManager()
    self.pluginManager.loadPlugins()

    # init select mapper
    self.selectMapper = {}

    for plug in self.pluginManager.plugins:
      if not self.selectMapper.has_key(plug.group):
        self.selectMapper[plug.group] = {}
        self.selectMapper[plug.group]['plugins'] = []
      self.selectMapper[plug.group]['plugins'].append(plug)

    for key, value in self.selectMapper.iteritems():
      # config push button
      button = QPushButton(key, self)
      button.setCheckable(True)
      self.ui.buttonVerticalLayout.addWidget(button)
      value['button'] = button

      # config widget group
      widget = QWidget(self)
      # widget.setMaximumWidth(300)
      layout = QFormLayout(widget)
      layout.addRow("<strong>%s</strong>" % key, QWidget(self))
      self.ui.widgetVerticalLayout.addWidget(widget)
      value['widget'] = widget

      # config all plugins' options
      for plug in value['plugins']:
        generateForm(layout, plug.options)

    # setup select mapper which defined in app/lib/select_mapper.py
    self.setupSelectMapper(self.selectMapper, self.ui.allButton)

    # config all buttons
    self.ui.allButton.setChecked(True)
    self.ui.pushButton.clicked.connect(self.scan)

  def scan(self):
    # init scan model
    scan = Scan()
    scan.scan_started_at = datetime.now()
    scan.scan_by = User.current_user()
    for key, value in self.selectMapper.iteritems():
      for plug in value['plugins']:
        options = getFormValue(plug.options)
        for ret in plug.execute(options):
          finding = Finding(**ret)
          finding.scan = scan
          finding.plugin_name = plug.name
          finding.plugin_group = plug.group
          finding.plugin_options = str(options)
          scan.findings.append(finding)
    scan.scan_finished_at = datetime.now()
    scan.findings_num = len(scan.findings)
    try:
      session.add(scan)
      session.add_all(scan.findings)
      session.commit()
    except IntegrityError, e:
      QMessageBox.information(self, u"SQL错误", u"扫描结果储存失败\n" + e.message)
