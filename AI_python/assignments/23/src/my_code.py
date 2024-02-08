#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 16 15:18:00 2023

testin  10 / 34 saa jatkuvasti nolla listalla :D

@author: sk
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
from scipy import stats

def splitXY(d):
    Y_column='DEATH_EVENT'
    return d.drop(Y_column, axis=1).to_numpy(), np.int32(d[Y_column]) 


def load_data(filename):
    global drop_columns
    data=pd.read_csv(filename)
    #set random order
    data=data.sample(frac=1).reset_index(drop=True)
    for col in drop_columns:
        data.drop(col, axis=1, inplace=True)

    return data    

def init_model(datafile):
    
    global model
    global drop_columns
    global scaler
    #global scaler
    #Modify this to drop unused columns from data
    drop_columns=[]

    data=load_data(datafile)
    
    #Modify this to drop unused columns from data
    
    drop_columns=[]

    data=load_data(datafile)
    data.dropna(inplace = True)
    
    
    columns = ["age", 'creatinine_phosphokinase','ejection_fraction', 'platelets','serum_creatinine','serum_sodium']
    
    for column in columns:
        z_threshold = 4.0
        z = np.abs(stats.zscore(data[column]))
        #outlier = (z >= z_threshold)
        filtered = (z < z_threshold)
        data = data[filtered]
    #your code here
    # - Preprocess data
    # - Split data into two pieces; train set and test set
    # - Create and train model
    # - y_test shall contain values 1/0
    data.drop_duplicates(inplace= True)
    traindata, testdata =train_test_split(data, test_size=60)
    x_train, y_train = splitXY(traindata)
    x_test, y_test = splitXY(testdata)
    #print(y_train.shape)
    
    scaler = preprocessing.MaxAbsScaler().fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
   
    n_train, width_train = np.shape(x_train)
    n_test, width_test = np.shape(x_test)
    
    assert(width_train==width_test)
    
    y_train = y_train.reshape(n_train,)
    
    # pca = PCA(6)
    # pca.fit(x_train)
    
    # pca.transform(x_train)
    
    # # plt.plot(pca.explained_variance_)
    # # plt.show()

    # # plt.plot(pca.explained_variance_)
    # # plt.semilogy()
    # # plt.show()
   
    model = Sequential()
    model.add(Dense(64,activation="relu", input_shape=(width_train,) ))
    model.add(Dropout(0.2))
    model.add(Dense(32,activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(32,activation="relu"))
    model.add(Dense(32,activation="relu"))
    model.add(Dense(1,activation="sigmoid" ))
    #model.summary()
    model.compile(loss="binary_crossentropy", optimizer="adam")
    model.fit(x_train,y_train
              #,batch_size=16
              , epochs = 60
              ,shuffle = True
              
              )

    return x_test, y_test #return test set

    

#input x is unscaled
def compute_value(x):
    global model
    
    global scaler
    #your code here
    x = scaler.transform(x)
    pred_y = model.predict(x)
    pred_y = np.round(pred_y)
    pred_y  = pred_y.reshape(x.shape[0],)
    # zeroes = 0
    # for y in pred_y:
    #     if y == 0:
    #         zeroes = zeroes + 1
    # print(zeroes)
    
    
    return pred_y


def validate(filename):
    data_val=load_data(filename)
    x_val, y_val=splitXY(data_val)
    y_pred=compute_value(x_val)
    return y_pred, y_val

if __name__ == "__main__":
    x_test, y_test=init_model('train.csv')

    testN, _=np.shape(x_test)
    assert(np.shape(y_test)==(testN,))

    y_pred=compute_value(x_test)
    errors=(y_pred!=y_test).sum()
    print('Errors (test set):', errors, '/', testN)


    #Just for testing that test.py will work 
    y_pred, y_val=validate('train.csv')
    valN=np.shape(y_val)[0]
    errors=(y_pred!=y_val).sum()
    #print('Errors (validation set):', errors, '/', valN)


    
    
