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
        eps=0.01
        a=np.array([1, 2, -1, 3])
        b=np.array([2, -2, -1, 1])

        phi=angle_between(a,b)
        phi_=1.407
        self.assertTrue(np.abs(phi-phi_)<eps)
        phi=angle_between(a,b)
        self.assertTrue(np.abs(phi-phi_)<eps)

        phi=angle_between(a,a)
        phi_=0.0
        self.assertTrue(np.abs(phi-phi_)<eps)
        phi=angle_between(b,b)
        self.assertTrue(np.abs(phi-phi_)<eps)

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

