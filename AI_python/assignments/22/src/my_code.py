#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: sk
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
#from keras.regularizers import l2
#from keras.optimizers import SGD
#Split data frame to x and y - don't modify
def splitXY(d):
    Y_column='fetal_health'
    return d.drop(Y_column, axis=1).to_numpy(), np.int32(d[Y_column]) 


def load_data(filename):
    global drop_columns
    data=pd.read_csv(filename)
    for col in drop_columns:
        data.drop(col, axis=1, inplace=True)

    return data    

def init_model(datafile):
    
    global model
    global drop_columns
    global scaler

    #Modify this to drop unused columns from data
    drop_columns=['histogram_width', 'histogram_min', "histogram_max","histogram_number_of_peaks",
                  'histogram_number_of_zeroes', 'histogram_mode', 'histogram_mean',
                  'histogram_median', 'histogram_variance', 'histogram_tendency']

    data=load_data(datafile) #load dataframe
    
    
    #your code here
    # - Preprocess data
    # - Split data into two pieces; train set and test set
    # - Create and train model
    # - y_test shall contain integer values in range 1..3
    # - Use global variables to store scaling information.
    #   You may need it in compute_value function.
    data.dropna(inplace=True)
    data.drop_duplicates(inplace= True)
    traindata, testdata =train_test_split(data, test_size=132)
    x_train, y_train = splitXY(traindata)
    x_test, y_test = splitXY(testdata)

    
    scaler = preprocessing.MinMaxScaler(feature_range=(-1,1)).fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    
    n_train, width_train = np.shape(x_train)
    
    num_classes = np.max(y_train) +1
    y_train = np_utils.to_categorical(y_train, num_classes)
    
    model = Sequential()
    model.add(Dense(32,activation = "relu", input_shape=(width_train,) ))
    model.add(Dense(32,activation="relu" ))
    model.add(Dropout(0.2))
    model.add(Dense(20,activation="relu"))
    model.add(Dense(20,activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(32,activation="relu"))
    model.add(Dense(32,activation="relu"))

    model.add(Dense(num_classes,activation="softmax"))
    model.summary()
    model.compile(loss="categorical_crossentropy",optimizer="adam")
    model.fit(x_train,y_train,batch_size=16, epochs = 20)
    
    
    return x_test, y_test #return test set for testing purposes


#Compute predicted value of x
def compute_value(x):
    global model
    global scaler
    
    
    #your code here
    # - x is unscaled x value, scale it
    # - utilize model to predict y_pred vector values, y_pred is vector which 
    #   elements are integers in 1..3
    x = scaler.transform(x)
    y_pred = model.predict(x)
    predY_int=np.round(y_pred)
    predY_int=predY_int.argmax(1)
    
    return predY_int

#Loads validation data set and computes predictions based on x-values
#Don't utilize y-values except for testing purposes!
def validate(filename):
    data_val=load_data(filename)
    x_val, y_val=splitXY(data_val)
    y_pred=compute_value(x_val)
    return y_pred, y_val


#Test program (don't modify)
if __name__ == "__main__":
    x_test, y_test=init_model('fetal_health.csv')

    testN, _=np.shape(x_test)
    assert(np.shape(y_test)==(testN,))

    y_pred=compute_value(x_test)
    errors=(y_pred!=y_test).sum()
    print('Errors (test set):', errors, '/', testN)

    y_pred, y_val=validate('validation.csv')
    valN=np.shape(y_val)[0]
    errors=(y_pred!=y_val).sum()
    print('Errors (validation set):', errors, '/', valN)


    
    