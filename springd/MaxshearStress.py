import math
import json
import sys
import os
def shear(D,K,P,d):
    T=(8*K*P*D)/(float(3.141)*(3*d))
    print('Maximum shear stress = ' ,T)
    return T
