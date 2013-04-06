#coding=utf-8

import inspect
from sqlalchemy import Integer, Float, String, Text, Boolean
from sqlalchemy import Time, Date, DateTime, ForeignKey
from sqlalchemy.dialects import postgresql
List = postgresql.ARRAY(String)
Double = Float

class Plugin(object):
  """Base class for plugin"""

  # a list of options
  # option include:
  #   title
  #   type: ( should in _validTypes )
  #   validator: lambda to validate if the option is valid
  #   additions fields ( optional ):
  #     tooltip
  #     maxValue, minValue for integer, double, time, date, datetime
  #     regex for string & text ( TODO )
  #     list ( a list of strings ) for list type ( must given if type is list )
  #     multiple == True, the list will be multiple choices
  # eg: options = [
  #   {'title': 'integer demo', 'type': Integer, 'minValue': 5, 'tooltip': 'integer demo tooltip'},
  #   {'title': 'double demo', 'type': Float, 'maxValue': 5},
  #   {'title': 'string demo', 'type': String},
  #   {'title': 'text demo', 'type': Text},
  #   {'title': 'boolean demo', 'type': Boolean},
  #   {'title': 'list demo', 'type': List, 'list': ['list 1', 'list 2']},
  #   {'title': 'time demo', 'type': Time, 'minValue': datetime.now(},
  #   {'title': 'date demo', 'type': Date, 'minValue': datetime.now(},
  #   {'title': 'datetime demo', 'type': DateTime, 'maxValue': datetime.now()},
  # ]
  options = []

  # Integer: spin box
  # Float: double spin box
  # String: line edit
  # Text: plain text edit
  # Boolean: check box
  # List: combo box
  # Time: time edit
  # Date: date edit
  # DateTime: date/time edit
  validTypes = (Integer, Float, String, Text, Boolean, List, Time, Date, DateTime)
  description = ''
  version = '0.0.1'

  def name():
    doc = "The name property."
    def fget(self):
      if not hasattr(self, '_name'):
        filename = inspect.getfile(self.__class__).split('/')[-1].split('.')[0]
        self._name = filename.decode('utf-8','ignore')
      return self._name
    def fset(self, value):
      self._name = value
    return locals()
  name = property(**name())

  def group():
    doc = "The group property."
    def fget(self):
      if not hasattr(self, '_group'):
        dirname = inspect.getfile(self.__class__).split('/')[-2]
        self._group = dirname.decode('utf-8','ignore')
      return self._group
    def fset(self, value):
      self._group = value
    return locals()
  group = property(**group())

  def __init__(self):
    pass

  def validateOptionsFormat(self):
    if not type(self.options) == list: 
      return "options should be a list"
    for option in self.options:
      if not option.has_key('title'): 
        return "option(%s) should has_key 'title'" % option
      if not option.has_key('type'): 
        return "option(%s) should has_key 'type'" % option
      if option['type'] == 'list' and not option.has_key('list'): 
        return "option(%s) should has_key 'list'" % option
      if not option['type'] in self.validTypes: 
        return "option(%s)['type'] should in validTypes" % option
    return None
  
  # argument options is a dict of options,
  #   whose key = option.title and value = option.value
  # this function should return a list of dict which include:
  #   severity
  #   message
  def execute(self, options={}):
    # return [{'severity':0, 'message':''}]
    return []