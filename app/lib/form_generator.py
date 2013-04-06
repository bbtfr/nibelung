# for options' (type: widget) Mapper
from PyQt4.QtGui import QSpinBox, QDoubleSpinBox, QLineEdit, QPlainTextEdit
from PyQt4.QtGui import QCheckBox, QComboBox, QTimeEdit, QDateEdit, QDateTimeEdit
from plugin import *

widgetMapper = {
  Integer: QSpinBox,
  Float: QDoubleSpinBox,
  String: QLineEdit,
  Text: QPlainTextEdit,
  Boolean: QCheckBox,
  List: QComboBox,
  Time: QTimeEdit,
  Date: QDateEdit,
  DateTime: QDateTimeEdit,
}

def generateForm(layout, options):
  """options should include keys 'title' and 'type'
     same as plugin options
  """
  # config all plugins' options
  for option in options:
    subWidget = widgetMapper[option['type']]()
    layout.addRow(option['title'], subWidget)
    if option['type'] in (Integer, Float):
      if option.has_key('minValue'):
        subWidget.setMinimum(option['minValue'])
      if option.has_key('maxValue'):
        subWidget.setMaximum(option['maxValue'])
    if option['type'] == List:
      subWidget.addItems(option['list'])
    if option['type'] in ('time', 'date', 'datetime'):
      if option.has_key('minValue'):
        subWidget.setMinimumDateTime(option['minValue'])
      if option.has_key('maxValue'):
        subWidget.setMaximumDateTime(option['maxValue'])
    if option.has_key('tooltip'):
      subWidget.setToolTip(option['tooltip'])
    option['widget'] = subWidget

def getFormValue(options):
  formValue = {}
  for option in options:
    if option['type'] == Text:
      formValue[option['title']] = unicode(option['widget'].toPlainText())
    elif option['type'] == List:
      formValue[option['title']] = unicode(option['widget'].currentText())
    else:
      formValue[option['title']] = unicode(option['widget'].text())
  return formValue

def setFormValue(options, formValue, cleanForm=True):
  for option in options:
    if formValue.has_key(option['title']):
      value = unicode(formValue[option['title']])
    else:
      if cleanForm:
        value = ''
      else:
        continue
    if option['type'] == Text:
      option['widget'].setPlainText(value)
    elif option['type'] == List:
      index = option['widget'].findData(value)
      if index > 0: 
        option['widget'].setCurrentIndex(index)
    else:
      option['widget'].setText(value)
  return formValue
