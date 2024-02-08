import sys
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
X=np.load('teach_data.npy')
Y=np.load('teach_class.npy')

################################################
#Your code below this line

train_percentage = 0.80
test_size = 0.20
#X, Y = shuffle(X, Y)
train_x, test_x, train_y,test_y =train_test_split(X, Y, train_size=train_percentage, test_size=test_size)

"""
# never use ... 
train_x = X[:train_percentage]
train_y = Y[:train_percentage]

test_x = X[train_percentage:]
test_y = Y[train_percentage:]
"""
"""
#standardize
stdev=train_x.std(axis = 0)
mean =train_x.mean(axis = 0)

train_x = (train_x - mean)/stdev 
test_x = (test_x - mean)/stdev 
"""

del X, Y

n_neighbors = 3
"""
model = KNeighborsClassifier(n_neighbors = n_neighbors)

"""
model = svm.SVC()

model.fit(train_x, train_y)

pred_y = model.predict(test_x) 

faulty = np.abs(np.abs(test_y)-np.abs(pred_y))

i = 0
for x in faulty:
    if x < 10: continue
    i = i + 1

precentage = i / faulty.shape[0]

print("faulty:", faulty)
print("counted:", i)
print("precentage:", precentage)

acc = accuracy_score(test_y, pred_y)

print('Accuracy =',acc)

#Your code above this line
################################################

print('Compute real predictions')
real_X=np.load('data_in.npy')

print('real_X -', np.shape(real_X))
pred = model.predict(real_X)
print('pred -', np.shape(pred))
np.save('data_classified.npy', pred)

