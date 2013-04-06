#coding=utf-8

from lib.plugin import *
from datetime import datetime

class SecondPlugin(Plugin):
  
  description = ""
  version = '0.0.1'
  options = [
    {'title': 'integer demo', 'type': Integer, 'minValue': 5, 'tooltip': 'integer demo tooltip'},
  ]

  def __init__(self):
    Plugin.__init__(self)
  
  def execute(self, options={}):
    return [{'severity':0, 'message':'exec function'}]
