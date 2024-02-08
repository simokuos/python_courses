import sys
import time

import numpy as np

def angle_between(a, b):
    angle = np.arccos(a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    return angle

