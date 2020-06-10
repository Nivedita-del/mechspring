import math
import json
from springd.meanCoilDia import MeanCoilDia
from springd.wireDia import Wire
from springd.springIndex import *
from springd.workFactor import *
from springd.MaxshearStress import *
from springd.Coils import *
from springd.Deflection import *

if __name__ == '__main__':
    x = int(input('Whats the outer diameter of the spring in mm?'))
    y = int(input('Whats the Inner diameter of the spring in mm?'))
    P = int(input("what is the load in N" ))
    G = int(input('Whatis modulus of rigidity? '))
    L_f = int(input('What is the desired free length? '))
    D = MeanCoilDia(x, y)
    d = Wire(x, y)
    C = spring(D,d)
    K = work(C)
    n = coil(G,L_f,P,D,d)
    spring(D, d)
    work(C)
    shear(D,K,P,d)
    coil(G,L_f,P,D,d)
    deflect(n, D,d, G, P)