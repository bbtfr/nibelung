#!/usr/bin/env python
#coding=utf-8

from controllers.login_controller import LoginController
from controllers.main_controller import MainController

# Just for testing, db migrate & seed
# import db_seed

import sys
from PyQt4.QtGui import QApplication

app = QApplication(sys.argv)

login = LoginController()
main = MainController()
# login.show()
# login.loggedin.connect(main.show)
main.show()

sys.exit(app.exec_())