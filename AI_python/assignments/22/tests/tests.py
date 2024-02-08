import unittest
from helpers import *
import numpy as np
from keras.models import load_model
import pandas as pd

#Remove if no python functions are not tested
from my_code import *


started_tests = 0
completed_tests = 0


class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        _, _=init_model('src/fetal_health.csv')

        y_pred, _=validate('tests/validation.csv')
        y_val=np.load('tests/validation_y.npy')
        valN=np.shape(y_val)[0]
        errors=(y_pred!=y_val).sum()

        limit=round(0.25*valN)
        print('errors =', errors, 'limit =', limit)

        self.assertTrue(errors <= limit)
        
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

