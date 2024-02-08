import numpy as np

npz_m4in = np.load("m4in.npz")
b = npz_m4in["b"]
np.save("m4out.npy", b)