import random
import unittest
import models
import config.db_seed

class TestModels(unittest.TestCase):

  def setUp(self):
    self.pluginManager = DirectoryPluginManager(echo=False)
    self.pluginManager.loadPlugins()

  def test_plugin_manager(self):
    self.assertNotEqual(len(self.pluginManager.plugins), 0)

  def test_each_plugin(self):
    for plug in self.pluginManager.plugins:
      self.assertIsNotNone(plug.name)
      self.assertIsNotNone(plug.group)

  def test_each_plugin_exec(self):
    for plug in self.pluginManager.plugins:
      results = plug.execute()
      for ret in results:
        self.assertIn('severity', ret)
        self.assertIn('message', ret)