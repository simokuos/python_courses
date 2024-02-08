import unittest
from helpers import *


started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        eps=0.2
        output=callpython(cmdline_args=[], input='').strip()
        x_est=float(output)
        x=14.035
        print("Estimated x =",x_est)
        self.assertTrue(x_est>x-eps and x_est<x+eps)
        self.endTest()

    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

