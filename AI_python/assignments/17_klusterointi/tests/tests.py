import unittest
from helpers import *

#Remove if no python functions are not tested
#from my_code import *


TEST_FUNCTION=False

started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        if not TEST_FUNCTION:
            self.startTest()
            self.assertEqual(callpython(cmdline_args=[], input='\n').strip(), '6')
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

