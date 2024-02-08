import unittest
from helpers import *
import os
import numpy as np

from my_code import *



started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        self.startTest()
        curdir=os.getcwd()
        os.chdir('src/')
        print('call init_model()')
        init_model()
        print('call compute_value()')
        test_x=np.load('../tests/x.npy')
        test_y=np.load('../tests/y.npy')
        pred_y=compute_value(test_x)
        os.chdir(curdir)
        MSE=mean_squared_error(test_y ,pred_y)
        print('MSE =', MSE)
        self.assertTrue(MSE<0.015)
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

