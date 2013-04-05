from datetime import datetime
from lib.plugin_manager import DirectoryPluginManager
from models import *

class ScanController:
  def scan(self):
    # init plugin manager
    pluginManager = DirectoryPluginManager()
    pluginManager.loadPlugins()

    # init scan model
    scan = Scan()
    scan.scan_start_at = datetime.now()
    scan.scan_by = User.current_user()
    for plug in pluginManager.plugins:
      options = {}
      for ret in plug.execute(options):
        finding = Finding(**ret)
        finding.scan = scan
        finding.plugin_name = plug.name
        finding.plugin_group = plug.group
        finding.plugin_options = str(options)
        print finding.message

    scan.scan_finish_at = datetime.now()
    scan.findings_num = len(scan.findings)
    scan.save()

  def show(self):
    pass
