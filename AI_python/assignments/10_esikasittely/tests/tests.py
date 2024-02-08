import unittest
from helpers import *
import pandas

started_tests = 0
completed_tests = 0

def rmoutput():
    try:
        os.remove('src/train.csv')
    except:
        pass
    try:
        os.remove('src/test.csv')
    except:
        pass


class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()

        rmoutput()
        callpython(cmdline_args=[], input='')
        
        trainfile='src/train.csv'
        testfile='src/test.csv'
        traindata=pandas.read_csv(trainfile)
        testdata=pandas.read_csv(testfile)

        rmoutput()
        
        train_rows=len(traindata)
        train_cols=len(traindata.columns)
        test_rows=len(testdata)
        test_cols=len(testdata.columns)

        train_rows_expected=140908
        train_cols_expected=3
        test_rows_expected=60389
        test_cols_expected=3

        print(train_rows, train_cols, test_rows, test_cols)

        
        row_epsilon=1000
        self.assertTrue(train_rows<train_rows_expected+row_epsilon)
        self.assertTrue(train_rows>train_rows_expected-row_epsilon)

        self.assertTrue(test_rows<test_rows_expected+row_epsilon)
        self.assertTrue(train_rows>train_rows_expected-row_epsilon)

        total_eps=100
        self.assertTrue((train_rows+test_rows)>(train_rows_expected+test_rows_expected-total_eps))
        self.assertTrue((train_rows+test_rows)<(train_rows_expected+test_rows_expected+total_eps))
        
        self.assertTrue(test_cols==test_cols_expected)
        self.assertTrue(train_cols==train_cols_expected)

        eps=0.00001
        self.assertTrue(traindata['data'].min()>-eps)
        self.assertTrue(traindata['data'].min()<0.3)
        self.assertTrue(traindata['data'].max()<1.0+eps)
        self.assertTrue(traindata['data'].max()>0.7)

        
        self.assertTrue(testdata['data'].min()>-eps)
        self.assertTrue(testdata['data'].min()<0.3)
        self.assertTrue(testdata['data'].max()<1.0+eps)
        self.assertTrue(testdata['data'].max()>0.7)
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

