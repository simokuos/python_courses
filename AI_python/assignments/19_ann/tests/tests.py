import unittest
from helpers import *
import numpy as np
from keras.models import load_model
import pandas as pd

#Remove if no python functions are not tested
#from my_code import *


started_tests = 0
completed_tests = 0

Y_column=8

def rmoutput():
    try:
        os.remove('src/kotilo.h5')
    except:
        pass


def splitXY(d):
    return d.drop(Y_column, axis=1), d[Y_column] 


class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        rmoutput()
        callpython(cmdline_args=[], input='')
        model=load_model('src/kotilo.h5')
        rmoutput()

        data=pd.read_csv('tests/measdata.csv', header=None)
        data.replace({'I':0, 'F':-1, 'M':1}, inplace=True)
        validX, validY=splitXY(data)

        validX=validX.to_numpy()
        validY=validY.to_numpy()

        n_test, _=np.shape(validX)

        predY=np.round(model.predict(validX)).reshape((n_test, ))

        accepted_n=(np.abs(predY-validY)<=3).sum()
        print('Correct predictions:', accepted_n, '/', n_test);

        self.assertTrue(accepted_n/n_test >= 0.7)
        
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

