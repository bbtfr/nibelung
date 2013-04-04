from plugins.plugin import Plugin

__all__ = ["FirstPlugin"]

class FirstPlugin(Plugin):
  
  description = ""
  version = '0.0.1'

  def __init__(self):
    Plugin.__init__(self)
  
  def execute(self, options={}):
    return [{'severity':0, 'message':'exec function'}]
