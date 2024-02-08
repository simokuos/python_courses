import unittest
from helpers import *
import numpy as np
from sklearn.metrics import accuracy_score

started_tests = 0
completed_tests = 0

def rmoutput():
    try:
        os.remove('src/data_classified.npy')
    except:
        pass


class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()

        rmoutput()
        
        callpython(cmdline_args=[], input='')
        Y_predict=np.load('src/data_classified.npy')
        Y_expected=np.load('tests/test_class.npy')

        rmoutput()
        
        print('Y_predict -', np.shape(Y_predict))
        print('Y_expected -', np.shape(Y_expected))
        limit=0.92
        acc = accuracy_score(Y_predict, Y_expected)
        print('Accuracy =',acc)
        self.assertTrue(acc>=limit)
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

