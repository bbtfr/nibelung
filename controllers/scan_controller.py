from plugins.plugin_manager import DirectoryPluginManager

class ScanController:
  def scan(self):
    pluginManager = DirectoryPluginManager()
    pluginManager.loadPlugins()
    for plug in pluginManager.plugins:
      print plug.options
      print plug.execute()