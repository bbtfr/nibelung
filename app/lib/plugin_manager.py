from plugin import Plugin
from imp import find_module, load_module, acquire_lock, release_lock
import os
import sys
import inspect

class PluginManager(object):
  """Base class for plugin managers. Does not implement loadPlugins, so it
  may only be used with a static list of plugins.
  """
  def __init__(self, plugins=(), config={}):
    self.__plugins = []
    if plugins:
      self.addPlugins(plugins)

  def __iter__(self):
    return iter(self.plugins)

  def addPlugin(self, plug):
    self.__plugins.append(plug)

  def addPlugins(self, plugins):
    for plug in plugins:
      self.addPlugin(plug)

  def delPlugin(self, plug):
    if plug in self.__plugins:
      self.__plugins.remove(plug)

  def delPlugins(self, plugins):
    for plug in plugins:
      self.delPlugin(plug)

  def getPlugins(self, name=None):
    plugins = []
    for plugin in self.__plugins:
      if (name is None or plugin.name == name):
        plugins.append(plugin)
    return plugins

  def _loadPlugin(self, plug):      
    loaded = False
    for p in self.plugins:
      if p.name == plug.name:
        loaded = True
        break
    if not loaded:
      self.addPlugin(plug)

  def loadPlugins(self):
    pass

  def _get_plugins(self):
    return self.__plugins

  def _set_plugins(self, plugins):
    self.__plugins = []
    self.addPlugins(plugins)

  plugins = property(_get_plugins, _set_plugins, None,
              """Access the list of plugins managed by
              this plugin manager""")
  
  
class DirectoryPluginManager(PluginManager):
  """Plugin manager that loads plugins from plugin directories.
  """
  def __init__(self, plugins=(), config={}):
    def default_directories(directories=[]):
      base_dir =  os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
      plugins_dir = os.path.join(base_dir, 'plugins')
      for d in os.listdir(plugins_dir):
        pd = os.path.join(plugins_dir, d)
        if os.path.isdir(pd):
          directories.append(pd)
      return directories
    self.directories = config.get("directories", default_directories())
    PluginManager.__init__(self, plugins, config)

  def loadPlugins(self):
    """Load plugins by iterating files in plugin directories.
    """
    plugins = []
    print 'Load Plugins from directories:', self.directories
    for dir in self.directories:
      try:
        for f in os.listdir(dir):
          if f.endswith(".py") and f != "__init__.py":
            plugins.append((f[:-3], dir))
      except OSError:
        print 'Failed to access:', dir
        continue

    fh = None
    mod = None
    for (name, dir) in plugins:
      try:
        acquire_lock()
        fh, filename, desc = find_module(name, [dir])
        print 'Load Plugin from file:', filename
        old = sys.modules.get(name)
        if old is not None:
          # make sure we get a fresh copy of anything we are trying
          # to load from a new path
          del sys.modules[name]
        mod = load_module(name, fh, filename, desc)
      except Exception as e:
        print '  Failed to load plugin,', e
        continue
      finally:
        if fh:
          fh.close()
        release_lock()
      for name, plug in inspect.getmembers(mod):
        if inspect.isclass(plug) and plug != Plugin:
          if not issubclass(plug, Plugin):
            # print '  Failed to load plugin, %s is not subclass of Plugin' % name 
            continue
          inst = plug()
          err = inst.validateOptionsFormat()
          if err:
            print '  Failed to load plugin,', err
            continue
          print '  Load Plugin:', inst.name
          self._loadPlugin(inst)
