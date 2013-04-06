from PyQt4.QtCore import pyqtSignal, SIGNAL, QSignalMapper, QObject

class SelectMapper:
  def setupSelectMapper(self, selectMapper, selectAllButton=None):
    """selectMapper should include keys 'button'(QPushButton) and 'widget'(QWidget)
    """
    self._select = None
    self.selectMapper = selectMapper
    self.selectAllButton = selectAllButton
    self.signalMapper = QSignalMapper(self)

    for key, value in self.selectMapper.iteritems():
      # config signal mapper
      value['button'].clicked.connect(self.signalMapper.map)
      self.signalMapper.setMapping(value['button'], key)

    # connect signal mapper to slot 'select' 
    QObject.connect(self.signalMapper, SIGNAL("mapped(QString)"), self.select)
    if selectAllButton:
      selectAllButton.clicked.connect(self.selectAll)

  def select(self, select):
    select = unicode(select)
    self.selectMapper[select]['button'].setChecked(True)
    if self._select == select: return
    if self._select:
      self.selectMapper[self._select]['button'].setChecked(False)
      self.selectMapper[self._select]['widget'].hide()
    else:
      if self.selectAllButton:
        self.selectAllButton.setChecked(False)
      for key, value in self.selectMapper.iteritems():
        value['widget'].hide()
    self.selectMapper[select]['widget'].show()
    self._select = select

  def selectAll(self):
    self.selectAllButton.setChecked(True)
    if self._select == None: return
    for key, value in self.selectMapper.iteritems():
      value['button'].setChecked(False)
      value['widget'].show()
    self._select = None