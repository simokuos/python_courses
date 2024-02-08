import sys
import time
import numpy as np
from sklearn.decomposition import PCA
from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

reduced_N=32

########################################################
#Write your code here
print(train_X.shape)
#Set value range -1..1
# color range 0 - 255
# Convert figures to vectors
def normalise_and_vector(matrix):
    matrix = matrix/128 -1
    matrix = matrix.reshape(matrix.shape[0],784)
    return matrix

train_X = normalise_and_vector(train_X)
test_X = normalise_and_vector(test_X)

#Compute reduced PCA

pca = PCA(32)

pca.fit(train_X) 
pca.fit

train_X_packed = pca.transform(train_X)#reduced dimension

test_X_packed = pca.transform(test_X)
#End of your code
########################################################
#Do not modify lines below this point!




#Save packed data
print('Save packed data')
np.save('packed_train.npy', train_X_packed)
np.save('packed_test.npy', test_X_packed)

if len(sys.argv)==1:
    #Test quality
    print('Train model')
    model = KNeighborsClassifier(n_neighbors = 11)
    model.fit(train_X_packed, train_Y)

    print('Compute predictions')
    pred = model.predict(test_X_packed)
    acc = accuracy_score(test_Y, pred)

    print('Accuracy =',acc)
