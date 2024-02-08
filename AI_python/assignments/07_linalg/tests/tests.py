import unittest
from helpers import *

#Remove if no python functions are not tested
from my_code import *

import numpy as np


started_tests = 0
completed_tests = 0

def random_three_vector():
    #By Andrew Bolster
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return np.array([x,y,z])

eps=0.0001

def is_same(a, b):
    for aa,bb in zip(a, b):
        if(np.abs(aa-bb)>eps):
            return False

    return True

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #my_code must be imported
        self.startTest()
        for _ in range(10):
            a_bar=random_three_vector()
            l=(0.1*10.0*np.random.rand())
            a=l*a_bar;
            self.assertTrue(is_same(a_bar, unit(a)))
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

