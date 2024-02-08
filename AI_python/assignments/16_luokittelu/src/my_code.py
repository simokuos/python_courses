import pandas 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import svm
#from sklearn.metrics import accuracy_score
filename1='grading.csv'
train_fraction = 0.8
Y_column='Passed'

#Load data
data=pandas.read_csv(filename1)
print("Read data shape = "+str(data.shape))
#print(data)


#################################################
#Your code here
#
#Create a classifier that classifies students

#esikasittely
data.dropna(inplace = True)
data.drop(["Name"], axis = 1, inplace=True)
print(data.shape)

def splitXY(d):
    return d.drop(Y_column, axis=1),d[Y_column]

traindata, testdata = train_test_split(data,test_size=1-train_fraction)
train_x, train_y = splitXY(traindata)
test_x, test_y = splitXY(testdata)

train_x = train_x.to_numpy()
test_x = test_x.to_numpy()

classifier = svm.SVC()
classifier.fit(train_x, train_y)

predY = classifier.predict(test_x)
"""
acc = accuracy_score(test_y, predY)
print('Accuracy =',acc)
"""
#
#################################################

#Load real data
filename2='assignments.csv'
data=pandas.read_csv(filename2)
names=data['Name']

#Remove name column
for col in ["Name"]:
    print("Remove "+col)
    data.drop(col, axis=1, inplace=True)
print()

print("Read data shape = "+str(data.shape))
print(data)
predY=classifier.predict(data)

#Create dataframe from numpy data
df = pandas.DataFrame({'Name': names, 'Passed': predY})
print(df)
df.to_csv('prediction.csv', index=False)

