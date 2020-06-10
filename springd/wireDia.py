import math
import json
import sys
import os
def Wire(x, y):
    d = x - y
    if (d<0):
        print('Wire Diameter = ', d)
        return d
    else:
        raise ("d is less ")
        print("invalid values")
        return 0