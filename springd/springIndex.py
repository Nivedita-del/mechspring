import math
import json
import sys
import os

def spring(D,d):

    if (d != 0 & d < 0):
        C = D / d
        print('Spring Index = ',C)
        return C
    else:
        print("Invalid values")
        raise("Invalid")
        return 0


