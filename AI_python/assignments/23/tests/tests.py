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

        retries=3

        for retry in range(retries):
            _, _=init_model('src/train.csv')

            y_pred, y_val=validate('tests/validation.csv')
            valN=np.shape(y_val)[0]
            errors=(y_pred!=y_val).sum()

            limit=np.round(0.3*valN)
            print('errors =', errors, 'limit =', limit)
            if errors<=limit:
                break

            
        
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

