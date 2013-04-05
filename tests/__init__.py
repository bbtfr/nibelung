#!/usr/bin/env python

import unittest, os

def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(this_dir)
    standard_tests.addTests(package_tests)
    return standard_tests
    