import unittest
from helpers import *
import numpy as np
from sklearn.decomposition import PCA
from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        callpython(cmdline_args=['a'], input='')

        (_, train_Y), (_, test_Y) = mnist.load_data()
        train_X_packed=np.load('src/packed_train.npy')
        test_X_packed=np.load('src/packed_test.npy')

        
        #Test quality
        print('Train model')
        model = KNeighborsClassifier(n_neighbors = 11)
        model.fit(train_X_packed, train_Y)

        print(np.shape(test_X_packed))
        print(np.shape(train_X_packed))

        self.assertTrue(np.shape(test_X_packed) == (10000, 32))
        self.assertTrue(np.shape(train_X_packed) == (60000, 32))

        print('Compute predictions')
        pred = model.predict(test_X_packed)
        acc = accuracy_score(test_Y, pred)

        print('Accuracy =',acc)
        self.assertTrue(acc>0.95)
        
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

