import sys
import time
import numpy as np

def unit(a):
    #laske yksikkövektori ^x = 1/||x|| * x
    unit_a = (1/np.linalg.norm(a)) * a
    return unit_a
