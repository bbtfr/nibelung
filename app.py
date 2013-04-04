#!/usr/bin/env python
#coding=utf-8

from config import engine, session
from plugins import *
from controllers.login_controller import LoginController
from controllers.main_controller import MainController

# Just for testing, db migrate & seed
import config.db_seed
import config.acl

class App:
  def __init__(self):
    login = LoginController()
    if login.login():
      main = MainController()
      main.show()

App()
