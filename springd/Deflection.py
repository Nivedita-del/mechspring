import math
import json
import sys
import os

def deflect(n, D,d, G, P):
    Df = (8 * P * (3 * D) * n) / (G* (4 ** d))
    print('Deflection of spring in mm = ',Df)
    return Df