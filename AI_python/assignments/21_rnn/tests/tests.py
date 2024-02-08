import unittest
from helpers import *
import numpy as np
from keras.models import load_model
import pandas as pd

#Remove if no python functions are not tested
from my_code import *


started_tests = 0
completed_tests = 0

Y_column=8
def splitXY(d):
    return d.drop(Y_column, axis=1), d[Y_column] 


class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        model=load_my_model('src/my_code.h5')

        X=np.load('tests/testx.npy')
        Y=np.load('tests/testy.npy')

        y_pred=compute_values(X)

        rmse = math.sqrt(mean_squared_error(Y, y_pred))
        
        limit=2.0
        print('RMSE: %.3f, required %.3f'%(rmse, limit))

        self.assertTrue(rmse <= limit)
        
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

