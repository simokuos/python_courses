import unittest
from helpers import *

#Remove if no python functions are not tested
from my_code import *
import numpy as np


started_tests = 0
completed_tests = 0

eps=0.0001

def is_same(a, b):
    for aa,bb in zip(a, b):
        if(np.abs(aa-bb)>eps):
            return False

    return True


class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        self.startTest()
        x=np.array([1.0, 2.0 , 3.4])
        y=np.array([-1.0, 0.5, 0])
        z=0.5*(x+y)
        Pz=project(z, 2*x)
        self.assertTrue(is_same(Pz, 0.5*x))

        x=np.array([2.0, 1.0, 2.0 , 3.4])
        y=np.array([-1.7, -1.0, 0.5, 1.0])
        z=(x+y)
        Pz=project(z, 2.2*x)
        self.assertTrue(is_same(Pz, x))

        x=np.array([2.0, 1.0, 2.0 , 2.4])
        y=np.array([-1.7, -1.0, 0.5, 1.0])
        z=(x+y)
        Pz=project(z, x)
        self.assertFalse(is_same(Pz, x))

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

