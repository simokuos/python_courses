import sys
import time
import pandas
from scipy import stats
import numpy as np
from sklearn import linear_model
#import matplotlib.pyplot as plt
inputfile='measurements.csv'
m=0.75 #mass of the object


#Your code here
with open(inputfile, encoding='utf-8') as f:
    data = pandas.read_csv(f)


#ominaislämpökapasiteetti : muutos( E )= c* m  * muutos(t): 
#c ominaislämpökapasiteetti, t lämpötila muutos, E energia, m on massa
#tarpeeseen muutettu kaava: c = (muutos(E)/muutos(t)) * 1/m
# tai suoran mukainen muutos(E) = 0 + cm * muutos(t), y = a + Bx


#esikasittely
data.dropna(inplace=True)


z_threshold = 3.0
z = np.abs(stats.zscore(data))
filtered = (z < z_threshold).all(axis=1)
data = data[filtered]


rows = data.shape[0]
x_matrix = data["T"].to_numpy().reshape((rows,1))
y_matrix = data["E"].to_numpy().reshape((rows,1))

L_reg = linear_model.LinearRegression()
L_reg.fit(x_matrix, y_matrix)
#print(L_reg.coef_[0,0])

coef = L_reg.coef_[0,0]
coef = coef * -1
c = coef / m

"""
#lineaarin kautta B(c*m) arvon selvitys
X_matrix = np.ones((data.shape[0],2))
X_matrix[:, 1] = data["T"]
Y_matrix = np.reshape(data["E"].values, (data.shape[0], 1))

ab = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y_matrix

a = ab[0,0]
b = ab[1,0]

a = a + b
a = a * m
"""
"""
fig = plt.figure(figsize=(16, 8))
plt.plot(x_matrix, y_matrix, "*")
plt.show()
"""

#print(data.shape)
#print(X_matrix.shape)

#Estimated specific heat capacity 
print(c)
