#from nose.tools import *
import unittest

import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    unittest.assertIs("egy", "kettő")
    print("I RAN!")