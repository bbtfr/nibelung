#!/usr/bin/env python

from plugins import *
from models import *
from controllers import *

login = LoginController()

if login.login():
  scan = ScanController()
  scan.scan()