import sys
import time
import numpy as np

def project(x, y):
    px = (x.dot(y) / y.dot(y))*y
    return px
