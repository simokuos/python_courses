import unittest
from helpers import *
import numpy as np

started_tests = 0
completed_tests = 0

def rmoutput():
    try:
        os.remove('src/out.npy')
    except:
        pass

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()

        rmoutput()
        callpython(cmdline_args=[], input='')
        inputfile='src/in.npy'
        outputfile='src/out.npy'

        data=np.load(inputfile)
        print('original shape =',np.shape(data))
        packed_data=np.load(outputfile)
        print('packed shape =',np.shape(packed_data))

        rmoutput()
        
        self.assertTrue(np.shape(data)[0]==np.shape(packed_data)[0])
        self.assertTrue(np.shape(packed_data)[1]>=20)
        self.assertTrue(np.shape(packed_data)[1]<=22)
        
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

