import inspect

class Plugin(object):

  options = []
  name = ''
  group = ''
  description = ''
  version = '0.0.1'

  def __init__(self):
    fa = inspect.getfile(self.__class__).split('/')
    self.name = fa[-1].split('.')[0]
    self.group = fa[-2]
  
  # should return a list of dict
  # the dict include:
  #   severity
  #   message
  def execute(self, options={}):
    # return [{'severity':0, 'message':''}]
    return []