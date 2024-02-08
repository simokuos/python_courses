import unittest
from helpers import *
import pandas

started_tests = 0
completed_tests = 0

def rmoutput():
    try:
        os.remove('src/prediction.csv')
    except:
        pass


class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        rmoutput()
        
        callpython(cmdline_args=[], input='')

        predictionfile='src/prediction.csv'
        realfile='tests/assignments.csv'

        pred_df=pandas.read_csv(predictionfile)
        real_df=pandas.read_csv(realfile)

        rmoutput()
        
        #Remove columns
        for col in ['Assignment A', 'Assignment B', 'Assignment C']:
            print("Remove "+col)
            real_df.drop(col, axis=1, inplace=True)
        print()

        correct=0
        total=len(real_df['Name'])
        
        for name in real_df['Name']:
            real_row=real_df[real_df['Name']==name]
            pred_row=pred_df[pred_df['Name']==name]
            if(real_row.iloc[0]['Passed']==pred_row.iloc[0]['Passed']):
                correct=correct+1
            else:
                print('Incorrect:', name)
        print(correct, '/', total)
        self.assertTrue(correct>=0.8*total)
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

