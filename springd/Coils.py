import math
import json
import sys
import os


def coil(G,L_f,P,D,d):
    n = float((G * (4 * d) * L_f) - (2 * G * (5 * d))) / ((G * (5 * d)) + (9.2 * P*(3 ** D)))
    print('Number of active coils = ',n)
    N = n + 2
    print('Total number of coils = ',N)
    return n

