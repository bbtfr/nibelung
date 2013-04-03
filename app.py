#!/usr/bin/env python
#coding=utf-8

from config import *
from plugins import *
from models import *
from controllers import *

# for testing
import db_seed

login = LoginController()

if login.login():
  scan = ScanController()
  scan.scan()
