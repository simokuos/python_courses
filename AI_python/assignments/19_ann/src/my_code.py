import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

Y_column=8

def splitXY(d):
    return d.drop(Y_column, axis=1), d[Y_column] 

data=pd.read_csv('traindata.csv', header=None)
#Your code here...


data[0].replace(["F","I","M"],[-1,0,1], inplace = True)

traindata, testdata = train_test_split(data, test_size = 0.2)
trainX, trainY = splitXY(traindata)
testX, testY = splitXY(traindata)
"""
#standardize data
stdev = trainX.std(axis=0)
mean = trainX.mean(axis=0)
trainX = (trainX - mean)/stdev
testX = (testX - mean)/stdev
"""
trainX = trainX.to_numpy()
testX = testX.to_numpy()
trainY = trainY.to_numpy()
testY = testY.to_numpy()

n_train, width_train = np.shape(trainX)
n_test, width_test = np.shape(testX)
model = Sequential()
model.add(Dense(32,activation = "relu", input_shape=(width_train,)))
model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='linear'))

model.summary()
model.compile(loss="mse")
model.fit(trainX,trainY, epochs = 10)

predY=model.predict(testX)


model.save('kotilo.h5')

predY=np.round(model.predict(testX)).reshape((n_test, ))

accepted_n=(np.abs(predY-testY)<=3).sum()
print('Correct predictions:', accepted_n, '/', n_test);
print("precentage:", (accepted_n/n_test)*100)
