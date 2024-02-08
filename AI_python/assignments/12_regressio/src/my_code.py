import sys
import time
import pandas
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

inputfile='mittaus.csv'


with open(inputfile, encoding='utf-8') as f:
    data = pandas.read_csv(f)
#Your code here
#print(data.shape)
#print(data.columns)

modeldegree = 2


rows = data.shape[0]
x_matrix = data["x"].to_numpy().reshape((rows,1))
y_matrix = data["y"].to_numpy().reshape((rows,1))

"""
line_reg = linear_model.LinearRegression()
line_reg.fit(x_matrix, y_matrix)

y_estimate = line_reg.predict(x_matrix)
"""

poly_reg = PolynomialFeatures(degree = modeldegree)
x_poly = poly_reg.fit_transform(x_matrix)

line_reg = linear_model.LinearRegression()
line_reg.fit(x_poly, y_matrix)

y_estimate = line_reg.predict(poly_reg.fit_transform(x_matrix))

a = line_reg.coef_[0,2]
b = line_reg.coef_[0,1]
c = line_reg.intercept_[0]

roots = np.roots([a,b,c])


"""
fig = plt.figure(figsize=(18, 8))
plt.plot(data["x"], data["y"], "*")
plt.plot(x_matrix, y_estimate, color="blue")

plt.show()
"""

#Print your solution
print(roots[0] )