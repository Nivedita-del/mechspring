import math
import json
import sys
import os

def work(C):
    K = ((4 * C - 1) / (4 * C - 4)) + ((float(0.615) / C))
    print("Whal's factor(K) = ",K)
    return K