import numpy as np

a = np.load("m2in.npy")

#a[0,0] = 1 #first number

a[-1, -1] = -1 #last number

np.save("m2out.npy", a)
