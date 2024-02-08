import unittest
from helpers import *
import pandas

started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        callpython(cmdline_args=[], input='')

        inputfile='src/preprocessed.csv'
        data=pandas.read_csv(inputfile)
        self.assertEqual(str(data.shape), str((13949, 70)))
        colsum=data['HR_radiation_direct_horizontal'].sum()
        #print(colsum)
        eps=100
        cs=3258483.278
        self.assertTrue((colsum<cs+eps) and (colsum>cs-eps))
        colsum=data.iloc[0, :].sum()
        eps=10
        cs=4471
        self.assertTrue((colsum<cs+eps) and (colsum>cs-eps))
        #print(colsum)
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

