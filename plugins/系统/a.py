#coding=utf-8

from lib.plugin import *
from datetime import datetime

class FirstPlugin(Plugin):
  
  description = ""
  version = '0.0.1'
  options = [
    {'title': 'integer demo', 'type': Integer, 'minValue': 5, 'tooltip': 'integer demo tooltip'},
    {'title': 'double demo', 'type': Float, 'maxValue': 5},
    {'title': 'string demo', 'type': String},
    {'title': 'text demo', 'type': Text},
    {'title': 'boolean demo', 'type': Boolean},
    {'title': 'list demo', 'type': List, 'list': ['list 1', 'list 2']},
    {'title': 'time demo', 'type': Time, 'minValue': datetime.now()},
    {'title': 'date demo', 'type': Date, 'minValue': datetime.now()},
    {'title': 'datetime demo', 'type': DateTime, 'maxValue': datetime.now()},
  ]

  def __init__(self):
    Plugin.__init__(self)
  
  def execute(self, options={}):
    return [{'severity':0, 'message':'exec function'}]
