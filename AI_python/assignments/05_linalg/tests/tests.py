import unittest
from helpers import *

#Remove if no python functions are not tested
from my_code import *
import numpy as np

started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #my_code must be imported
        self.startTest()
        a=np.array([0.1,0.2,0.3])
        b=np.array([0.3,0.0,-0.1])
        c=np.array([-0.3,0.1,-0.1])
        self.assertTrue(is_orthogonal(a, b))
        self.assertTrue(is_orthogonal(b, a))
        self.assertFalse(is_orthogonal(c, a))
        self.assertFalse(is_orthogonal(a, a))
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

