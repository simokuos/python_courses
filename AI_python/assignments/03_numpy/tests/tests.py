import unittest
from helpers import *
import numpy as np


started_tests = 0
completed_tests = 0

def rmoutput():
    try:
        os.remove('src/ab.npz')
    except:
        pass


class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        rmoutput()
        callpython()
        a_=np.load('src/a.npy')
        b_=np.load('src/b.npy')
        ab=np.load('src/ab.npz')
        rmoutput()
        a=ab['a']
        b=ab['b']
        #Test correct size
        self.assertTrue(np.size(a_)==np.size(a))
        self.assertTrue(np.size(b_)==np.size(b))
        #Check all elements
        self.assertTrue((a_==a).all())
        self.assertTrue((b_==b).all())
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

