import math
import json
import sys
import os

def MeanCoilDia(x, y):
    #mean dia meter
    if (x>y):
        D = (x+y)/2
        print('Mean coil diameter = ', D)
        return D
    else:
        raise ("x is less")
        return -1

