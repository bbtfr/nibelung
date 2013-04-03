from plugins.plugin import Plugin

__all__ = ["FirstPlugin"]

class FirstPlugin(Plugin):
  
  name = "firstPlugin"
  description = ""
  version = '0.0.1'

  def __init__(self):
    Plugin.__init__(self)
  
  def scan(self, options={}):
    return "exec function"