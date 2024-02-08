import sys
import time
import numpy as np


def is_orthogonal(a, b):
    
    #angle a = x, b = y ; x.y / ||x*y||
    #np.arccos(x_vektori.dot(y_vektori)/(np.linalg.norm(x_vektori)*np.linalg.norm(y_vektori)))) #basic_mariisi.py in harjoitukset
    is_orthogonal_angle = False
    angle = np.arccos(a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    
    #test for rigth angle
    #rigth angle is 1/2 * pi
    rigth_angle = 1/2 * np.pi
    if(angle == rigth_angle or (angle * -1) == rigth_angle):
        is_orthogonal_angle = True
    
    return is_orthogonal_angle

"""
vektori1 = np.array([1,0])
vektori2 = np.array([0,1])
vektori3 = np.array([2,1])

print(is_orthogonal(vektori1, vektori2))
print(is_orthogonal(vektori1, vektori3))
"""