#!/usr/bin/python

import math
import numpy as np

k=1
# J/K
kB = 1.3806505*(10**(-23))
# K
T = 273 + 10
# J*s
h = 6.62607015*(10**(-34))
# kcal/(K*mol)
R = 1.987*(10**(-3))
# s-1
ka = 24.3612
# s-1
kb = 442.2197

Ga = -R * T * math.log((ka*h)/(kB*T))

print 'Ga = ',Ga

Gb = -R * T * math.log((kb*h)/(kB*T))

print 'Gb = ',Gb

